from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt 
from src.config import Config
import uuid
import logging

passwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ACCESS_TOKEN_EXPIRY = 3600  # 1 hour in seconds

def generate_password_hash(password: str) -> str:
    """Generate a hashed password."""
    hash= passwd_context.hash(password)
    
    
    return hash


def verify_password(password: str,hash: str) -> bool:
    """Verify a password against a hash."""
    return passwd_context.verify(password, hash)



def create_access_token(user_data:dict,expiry:timedelta = None,refresh:bool = False):

    payload = {}
    payload["user"] = user_data
    payload["exp"] = datetime.now() + expiry if expiry is not None else datetime.now() + timedelta(seconds=ACCESS_TOKEN_EXPIRY)
    payload["jti"] = str(uuid.uuid4())
    payload["refresh"] = refresh

    token = jwt.encode(
        payload=payload,
        key=Config.JWT_SECRET_KEY,
        algorithm=Config.JWT_ALGORITHM
    )
    return token


def decode_token(token: str) -> dict:
    try:
        # Decode the JWT token using the secret key and algorithm
        token_data = jwt.decode(
            token,
            key=Config.JWT_SECRET_KEY,
            algorithms=[Config.JWT_ALGORITHM]
        )
        return token_data

    except jwt.PyJWTError as e:
        logging.exception(e)
        return None