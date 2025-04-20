from passlib.context import CryptContext


passwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def generate_password_hash(password: str) -> str:
    """Generate a hashed password."""
    hash= passwd_context.hash(password)
    
    
    return hash


def verify_password(password: str,hash: str) -> bool:
    """Verify a password against a hash."""
    return passwd_context.verify(password, hash)