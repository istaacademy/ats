import hmac 
import hashlib
import time
import base64
import os

SECRET_KEY = os.getenv('SECRET_KEY')



def generate_token(username):
    timestamp = str(int(time.time()))
    message = f"{username}:{timestamp}"

    signature = hmac.new(SECRET_KEY.encode(),message.encode()
                         ,hashlib.sha256).hexdigest()
    
    token = f"{message}:{signature}"
    token_based64 = base64.b64decode(token.encode()).decode

    return token_based64


def refresh_token(old_token):
    old_token_decoded = base64.b64decode(old_token.encode()).decode()
    
    username, old_timestamp, old_signature = old_token_decoded.split(':')
    
    new_token = generate_token(username)
    
    return new_token

def validate_token(token):
    try:
        token_decoded = base64.b64decode(token.encode()).decode()
        
        username, timestamp, signature = token_decoded.split(':')
        
        message = f"{username}:{timestamp}"
        
        expected_signature = hmac.new(SECRET_KEY.encode(), message.encode(), hashlib.sha256).hexdigest()
        
        if hmac.compare_digest(signature, expected_signature):
            return username
        else:
            return None
    except:

        return None