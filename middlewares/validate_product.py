"""
Order Request Validation Middleware

This module provides a middleware for validating order requests.

Middleware:
    - validate_order_request: Validates the order request data.

"""

from functools import wraps
from flask import request
from utilities.request_handlers import invalid_request_handler

def validate_order_request(func):
    """
    Validates the order request data.

    Args:
        func (function): The route handler function.

    Returns:
        function: The wrapper function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Request validation
        body = request.json
        product_id = body.get('product_id')
        quantity = body.get('quantity')
        card_number = body.get('card_number')
        exp_date = body.get('exp_date')
        csv = body.get('csv') 

        if not body or not product_id or not quantity or not card_number or not exp_date or not csv :
            return invalid_request_handler()
        
        # Call the route handler if the request is valid
        return func(*args, **kwargs)
    
    return wrapper
