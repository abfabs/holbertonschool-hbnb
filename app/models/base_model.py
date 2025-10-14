import uuid
from datetime import datetime


class BaseModel:
    # Initialize a new instance with a unique ID and timestamps
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    # Update the updated_at timestamp to the current time
    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()


    # Update object attributes from a dictionary and save the changes
    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()
