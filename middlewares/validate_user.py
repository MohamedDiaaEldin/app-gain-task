"""
Authentication and Request Validation Middlewares

This module provides middlewares for authentication and request validation.

Middlewares:
    - authenticate: Middleware to ensure user authentication.
    - validate_register_request: Middleware to validate registration requests.
    - validate_login_request: Middleware to validate login requests.

"""

from functools import wraps
from flask import request
from utilities.jwt_generator import is_valid_jwt
from utilities.request_handlers import invalid_request_handler, unauthorized_handler


def authenticate(func):   
    """
    Middleware to ensure user authentication.

    Args:
        f (function): The route handler function.

    Returns:
        function: The wrapper function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Request validation 
        access_token = request.cookies.get('access_token')
        if not access_token or not is_valid_jwt(access_token):
            return unauthorized_handler()
        # Call the route handler if the request is valid
        return func(*args, **kwargs)
    return wrapper



def validate_register_request(func):
    """
    Middleware to validate registration requests.

    Args:
        func (function): The route handler function.

    Returns:
        function: The wrapper function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Request validation 
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
    """
    Middleware to validate login requests.

    Args:
        func (function): The route handler function.

    Returns:
        function: The wrapper function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Request validation 
        body = request.json
        email = body.get('email')
        password = body.get('password')
        if not body or not email or not password:
            return invalid_request_handler()
        # Call the route handler if the request is valid
        return func(*args, **kwargs)
    return wrapper
