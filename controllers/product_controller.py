
from middlewares.validate_user import authenticate

@authenticate
def order(): 
    return 'hi'
    pass