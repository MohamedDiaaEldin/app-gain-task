

from functools import wraps

from flask import request, jsonify

from utilities.jwt_generator import is_valid_jwt


def authenticate(f):   
    @wraps(f)
    def is_authenticated(*args, **kwargs):
        user_jwt = request.cookies.get('access_token')
        print(user_jwt)
        print(is_valid_jwt(user_jwt))
        if not (user_jwt and is_valid_jwt(user_jwt)):
            return jsonify({
                'message':'unauthorized'
            }, 401)
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
            return jsonify({'error': 'Invalid data'}), 400
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
            return jsonify({'error': 'Invalid data'}), 400
        # Call the route handler if the request is valid
        return func(*args, **kwargs)
    return wrapper
