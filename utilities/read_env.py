import os
from dotenv import load_dotenv


path = None
def get_env(key):  
    if path : 
        load_dotenv(path)
    else : 
        load_dotenv()
    value = os.getenv(key)
    return value