"""
security.py

Handles security-related functions like password hashing and verification.
"""
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Hashes a password using bcrypt."""


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a plain password against its hashed version."""


# --- Encryption/Decryption for sensitive data ---

"""
This is how I imagine making sure that the secretes can only be used 
from device that the person controlls


ENCRYPTION_KEY = os.getenv("APP_ENCRYPTION_KEY")
if ENCRYPTION_KEY is None:
    raise ValueError("APP_ENCRYPTION_KEY environment variable not set. Please generate one and add it to your .env file.")
try:
    fernet = Fernet(ENCRYPTION_KEY.encode())
except Exception as e:
    raise ValueError(f"Invalid APP_ENCRYPTION_KEY: {e}. Ensure it's a valid Fernet key.")
"""

def encrypt_secret(data: str) -> str:
    """Encrypts a string using the master encryption key. Using fernet"""
    


def decrypt_secret(encrypted_data: str) -> str:
    """Decrypts an encrypted string using the master encryption key. Using fernet"""
    
