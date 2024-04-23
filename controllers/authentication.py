from middlewares.validate_user import authenticate, validate_login_request, validate_register_request
from models.user import User
from database import db
from flask import request, make_response
from utilities.password import hash_password, check_password
from utilities.jwt_generator import generate_jwt
from utilities.request_handlers import conflict_handler, not_found_handler, server_error_handler, success_handler,  unauthorized_handler



@validate_register_request
def register_user():
    try:
        # check if user is registered 
        body = request.json
        user  = User.get_user_by_email(body.get('email'))
        if user : 
            return conflict_handler() 
        # Register New User 

        # Hash User Password
        hashed_password = hash_password(body.get('password'))
        print(hashed_password)
        new_user  = User(username=body.get('username'), email=body.get('email'), address=body.get('email'), password=hashed_password)    
        db.session.add(new_user)
        db.session.commit()
        print('New User is added')
        return success_handler()
    except : 
        print('Error Happened While Adding new User')
        db.session.rollback()
        db.session.close()
        return server_error_handler()
    finally: 
        db.session.close()


@validate_login_request
def login(): 
    try: 
        ## check if user is registered
        body = request.json
        user  = User.get_user_by_email(body.get('email')) 
        if not user : 
            return not_found_handler()
        
        # validate user password
        if not check_password(body.get('password'), user.password) : 
            return unauthorized_handler()
        
        res = make_response(success_handler())                
        # set access token in cookies
        res.set_cookie('access_token', generate_jwt({'email': body.get('email')}))                
        return res
    except : 
        return server_error_handler()    
    finally: 
        db.session.close()


@authenticate
def logout(): 
    try : 
        res = make_response(success_handler())
        res.set_cookie('access_token', '')                
        
        return res
    except : 
        return server_error_handler()

