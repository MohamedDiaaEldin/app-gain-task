"""
Product Ordering API

This module provides an endpoint for ordering products.

Endpoint:
    - /order (POST): Place an order for a product.

Middleware:
    - authenticate: Middleware to ensure user authentication.
    - validate_order_request: Middleware to validate order request data.

"""

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
    """
    Place an order for a product.

    Returns:
        Response: Success or error response.
    """
    try: 
        body = request.json
        quantity =  body.get('quantity')
        access_token  = request.cookies.get('access_token')
        
        product = Product.get_product_by_id(body.get('product_id')) 
        if not product or product.quantity < quantity: 
            return not_found_handler()
        
        product.quantity = product.quantity - quantity
        
        user = User.get_user_by_email(decode_jwt(access_token)['email'])    
        new_purchase = Purchase(user_id=user.id, product_id=product.id, cost=quantity*product.price)

        db.session.add(new_purchase)
        db.session.commit()
        
        return success_handler()
    except : 
        db.session.rollback()
        return server_error_handler()
    finally :
        db.session.close()
