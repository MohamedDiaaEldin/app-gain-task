"""
User Authentication API

This module provides endpoints for user registration, login, and logout.

Endpoints:
    - /register (POST): Register a new user.
    - /login (POST): Log in an existing user.
    - /logout (GET): Log out the currently authenticated user.

Middleware:
    - authenticate: Middleware to ensure user authentication.
    - validate_login_request: Middleware to validate login request data.
    - validate_register_request: Middleware to validate register request data.

"""

from middlewares.validate_user import authenticate, validate_login_request, validate_register_request
from models.user import User
from database import db
from flask import request, make_response
from utilities.password import hash_password, check_password
from utilities.jwt_generator import generate_jwt
from utilities.request_handlers import conflict_handler, not_found_handler, server_error_handler, success_handler, unauthorized_handler


@validate_register_request
def register_user():
    """
    Register a new user.

    Returns:
        Response: Success or error response.
    """
    try:
        body = request.json
        user = User.get_user_by_email(body.get('email'))
        if user:
            return conflict_handler()

        hashed_password = hash_password(body.get('password'))
        new_user = User(username=body.get('username'), email=body.get('email'), address=body.get('address'), password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return success_handler()
    except:
        db.session.rollback()
        return server_error_handler()
    finally:
        db.session.close()


@validate_login_request
def login():
    """
    Log in an existing user.

    Returns:
        Response: Success or error response.
    """
    try:
        body = request.json
        user = User.get_user_by_email(body.get('email'))
        if not user:
            return not_found_handler()

        if not check_password(body.get('password'), user.password):
            return unauthorized_handler()

        res = make_response(success_handler())
        res.set_cookie('access_token', generate_jwt({'email': body.get('email')}))
        return res
    except:
        return server_error_handler()
    finally:
        db.session.close()


@authenticate
def logout():
    """
    Log out the currently authenticated user.

    Returns:
        Response: Success or error response.
    """
    try:
        res = make_response(success_handler())
        res.set_cookie('access_token', '')
        return res
    except:
        return server_error_handler()
