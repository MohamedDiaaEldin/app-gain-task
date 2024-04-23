import jwt

from .read_env import get_env
from datetime import datetime, timedelta, timezone



JWT_SECRET = get_env('JWT_SECRET')
ALGORITHM = "HS256"



def generate_jwt(payload):
    # Set expiration time to 2 day from now
    exp_time = datetime.now(timezone.utc) + timedelta(days=2)
    payload['exp'] = exp_time.timestamp()
    return jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)


def is_valid_jwt(token):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        return True
    except jwt.ExpiredSignatureError:
        print('Token has expired')
        return False
    except jwt.InvalidTokenError:
        print('Invalid token')
        return False
    
def decode_jwt(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=ALGORITHM)
    except:
        return None


