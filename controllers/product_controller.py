
from flask import request
from middlewares.validate_product import validate_order_request
from middlewares.validate_user import authenticate
from models.product import Product
from models.purchase import Purchase
from models.user import User
from database import db
from utilities.jwt_generator import decode_jwt
from utilities.request_handlers import not_found_handler, server_error_handler, success_handler

@authenticate
@validate_order_request
def order(): 
    try: 
        # check if product and quantity availability
        body = request.json
        quantity =  body.get('quantity')
        access_token  = request.cookies.get('access_token')
        
        product = Product.get_product_by_id(body.get('product_id')) 
        if not product or product.quantity < quantity: 
            return not_found_handler()
        

        ## call the payment gateway 

        ## update the quantify 
        product.quantity = product.quantity - quantity
        
        user = User.get_user_by_email( decode_jwt(access_token)['email'])    
        ## update the purchases table 
        new_purchase = Purchase(user_id=user.id, product_id=product.id, cost=quantity*product.price)

        db.session.add(new_purchase)
        db.session.commit()
        
        print('Product Purchased Successfully')
        return success_handler()
    except : 
        db.session.rollback()
        ## get the money back 
        return server_error_handler()
    finally :
        db.session.close()
        