"""
Product Ordering API

This module provides an endpoint for ordering products.

Endpoint:
    - /order (POST): Place an order for a product.

Middleware:
    - authenticate: Middleware to ensure user authentication.
    - validate_order_request: Middleware to validate order request data.

"""
import threading
from flask import make_response, request
from middlewares.validate_product import validate_order_request
from middlewares.validate_user import authenticate
from models.product import Product
from models.purchase import Purchase
from models.user import User
from models.user_account import UserAcount
from database import db
from utilities.email_service import send_order_confirmation_email
from utilities.jwt_generator import decode_jwt
from utilities.request_handlers import not_found_handler, server_error_handler, success_handler, unauthorized_handler
from sqlalchemy.orm import sessionmaker

@authenticate
@validate_order_request
def  order(): 
    """
    Place an order for a product.

    Returns:
        Response: Success or error response.
    """
    paid = False
    committed = False
    cost = 0
    # Create a new session
    Session = sessionmaker(bind=db.engine)
    session = Session()

    try: 
        # Retrieve JSON data from the request
        body = request.json
        quantity =  body.get('quantity')
        access_token  = request.cookies.get('access_token')

        # Validate Quantity  
        product = session.query(Product).filter(Product.id == body.get('product_id')).first() 
        if not product or product.quantity < quantity: 
            return not_found_handler()
        
        ## Get User Data
        user = session.query(User).filter(User.email == decode_jwt(access_token)['email']).first()

        if not user :             
            res = make_response(unauthorized_handler())
            res.set_cookie('access_token', '')
            return res

        # Calculates Order Cost 
        cost = quantity * product.price
        

        # Payment Process
        status_code =  UserAcount.process_payment({
            'card_number' : body.get('card_number'), 
            'exp_date': body.get('exp_date'), 
            'csv' : body.get('csv'), 
            'amount' : cost        
        })
        
        if status_code == 404 : 
            return not_found_handler('Payment Account Not Found Or Not Enough Balance')
        elif status_code == 500 : 
            return server_error_handler('Error Processing Payment')
        else : 
            paid = True
            print('User Paid: ', cost)


        ## Update Stock Quantity
        product.quantity = product.quantity - quantity

        
        ## Create New Purchase With Order Details
        new_purchase = Purchase(user_id=user.id, product_id=product.id, cost=cost, quantity=quantity, paid=paid)
        
        ## Commit Changes
        session.add_all([new_purchase, product])
        
        session.commit()       
        committed = True
        

        ## Send Email Async
        thr = threading.Thread( target=send_order_confirmation_email, args=(product.name, quantity, cost, user.email, user.address, user.username, new_purchase.id) )
        thr.start()
        
        # raise Error('For Testing')
        return success_handler()
    except :                 
        # Rollback changes if an error occurs during the transaction
        session.rollback()
        if paid and not committed: 
           status_code = UserAcount.add_balance({
            'card_number' : body.get('card_number'), 
            'exp_date': body.get('exp_date'), 
            'csv' : body.get('csv'), 
            'amount' : cost        
            }) 
        
           if status_code == 200 : 
               print('User Gets Money Back, Amount: ', cost)
           else : 
               print(f'Error Getting Back User Money, Amount: {cost}')
            
        return server_error_handler()
    finally :
        # Close the session after transaction completion or failure
        session.close()
