from app.models.base_model import BaseModel
import re

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = self.validate_first_name(first_name)
        self.last_name = self.validate_last_name(last_name)
        self.email = self.validate_email(email)
        self.is_admin = is_admin
        self.places = []  # List to store user's places

    def validate_first_name(self, first_name):
        """Validate first name: required, max 50 characters"""
        if not first_name or not isinstance(first_name, str):
            raise ValueError("First name is required and must be a string")
        if len(first_name) > 50:
            raise ValueError("First name must not exceed 50 characters")
        return first_name

    def validate_last_name(self, last_name):
        """Validate last name: required, max 50 characters"""
        if not last_name or not isinstance(last_name, str):
            raise ValueError("Last name is required and must be a string")
        if len(last_name) > 50:
            raise ValueError("Last name must not exceed 50 characters")
        return last_name

    def validate_email(self, email):
        """Validate email: required, proper format"""
        if not email or not isinstance(email, str):
            raise ValueError("Email is required and must be a string")
        # Basic email validation pattern
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            raise ValueError("Invalid email format")
        return email

    def add_place(self, place):
        """Add a place to the user's list of places"""
        self.places.append(place)
