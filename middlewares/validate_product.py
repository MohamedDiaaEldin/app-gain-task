



from functools import wraps

from flask import request

from utilities.request_handlers import invalid_request_handler


def validate_order_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # request validation 
        body = request.json
        product_id = body.get('product_id')
        quantity = body.get('quantity')

        if not body or not product_id or not quantity:
            return invalid_request_handler()
        # Call the route handler if the request is valid
        return func(*args, **kwargs)
    return wrapper
