# Create Hasher
from passlib.context import CryptContext

password_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


# Create Utility Class
class Hasher():
    """
    Here we create 2 functions to Verify | Hash the Password
    """

    @staticmethod
    def verify_password(plain_pass, hashed_pass):
        return password_context.verify(plain_pass, hashed_pass)  # Returns true/false

    @staticmethod
    def get_password_hash(plain_pass):
        return password_context.hash(plain_pass)
