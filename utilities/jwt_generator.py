import jwt
from datetime import datetime, timedelta, timezone
from .read_env import get_env



JWT_SECRET = get_env('JWT_SECRET')
ALGORITHM = "HS256"
EXP_IN = 2 # days


def generate_jwt(payload):
    # Set expiration time to 2 day from now
    exp_time = datetime.now(timezone.utc) + timedelta(days=EXP_IN)
    payload['exp'] = exp_time.timestamp()
    return jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)


def is_valid_jwt(token):
    try:
        jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
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


