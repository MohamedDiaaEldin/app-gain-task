
import bcrypt

used_encode = 'utf-8'
def hash_password(password):     
    try :
        return bcrypt.hashpw(password.encode(used_encode), bcrypt.gensalt()).decode(used_encode)
    except : 
        return None


def check_password(password, hashed_password): 
    print(password)
    print(hashed_password)

    try:         
        return  bcrypt.checkpw(password.encode(used_encode), hashed_password.encode(used_encode))   
    except : 
        return None
    


