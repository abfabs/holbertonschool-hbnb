from app.models.base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = self.validate_name(name)

    def validate_name(self, name):
        """Validate name: required, max 50 characters"""
        if not name or not isinstance(name, str):
            raise ValueError("Amenity name is required and must be a string")
        if len(name) > 50:
            raise ValueError("Amenity name must not exceed 50 characters")
        return name
