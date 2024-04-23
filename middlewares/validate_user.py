

from functools import wraps
from flask import request
from utilities.jwt_generator import is_valid_jwt
from utilities.request_handlers import invalid_request_handler, unauthorized_handler


def authenticate(f):   
    @wraps(f)
    def is_authenticated(*args, **kwargs):
        user_jwt = request.cookies.get('access_token')
        if not (user_jwt and is_valid_jwt(user_jwt)):
            return unauthorized_handler()
        return f(*args, **kwargs)
    return is_authenticated


def validate_register_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # request validation 
        body = request.json
        username = body.get('username')
        email = body.get('email')
        address = body.get('address')
        password = body.get('password')
        if not body or not username or not email or not address or not password:
            return invalid_request_handler()
        # Call the route handler if the request is valid
        return func(*args, **kwargs)
    return wrapper



def validate_login_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # request validation 
        body = request.json
        email = body.get('email')
        password = body.get('password')
        if not body  or not email or not password:
            return invalid_request_handler()
        # Call the route handler if the request is valid
        return func(*args, **kwargs)
    return wrapper
