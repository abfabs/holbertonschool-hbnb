from app.models.base_model import BaseModel
import re
from app.extentions import bcrypt

class User(BaseModel):
    # Initialize a new user with validated attributes
    def __init__(self, first_name, last_name, email, is_admin=False, password=None):
        super().__init__()
        self.first_name = self.validate_first_name(first_name)
        self.last_name = self.validate_last_name(last_name)
        self.email = self.validate_email(email)
        self.is_admin = is_admin
        self.password = None
        self.places = []  # List to store user's places

        if password:
            self.hash_password(password)


    # Validate that the first name is a non-empty string within length limits
    def validate_first_name(self, first_name):
        """Validate first name: required, max 50 characters"""
        if not first_name or not isinstance(first_name, str):
            raise ValueError("First name is required and must be a string")
        if len(first_name) > 50:
            raise ValueError("First name must not exceed 50 characters")
        return first_name


    # Validate that the last name is a non-empty string within length limits
    def validate_last_name(self, last_name):
        """Validate last name: required, max 50 characters"""
        if not last_name or not isinstance(last_name, str):
            raise ValueError("Last name is required and must be a string")
        if len(last_name) > 50:
            raise ValueError("Last name must not exceed 50 characters")
        return last_name


    # Validate that the email is a non-empty string matching proper email format
    def validate_email(self, email):
        """Validate email: required, proper format"""
        if not email or not isinstance(email, str):
            raise ValueError("Email is required and must be a string")
        # Basic email validation pattern
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            raise ValueError("Invalid email format")
        return email


    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)


    # Add a place to the user's list of associated places
    def add_place(self, place):
        """Add a place to the user's list of places"""
        self.places.append(place)

