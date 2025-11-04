from app.models.basemodel import BaseModel
from app.extensions import db

class Amenity(BaseModel):
    __tablename__ = 'amenities'
    
    name = db.Column(db.String(100), nullable=False)
    
    def __init__(self, name):
        super().__init__()
        self.name = self.validate_name(name)
    
    def validate_name(self, name):
        """Validate that the name is a non-empty string within length limits"""
        if not name or not isinstance(name, str):
            raise ValueError("Amenity name is required and must be a string")
        if len(name) > 100:
            raise ValueError("Amenity name must not exceed 100 characters")
        return name
