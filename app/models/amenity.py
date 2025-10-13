from app.models.base_model import BaseModel


class Amenity(BaseModel):
    # Initialize a new amenity with a validated name
    def __init__(self, name):
        super().__init__()
        self.name = self.validate_name(name)


    # Validate that the amenity name is a non-empty string within length limits
    def validate_name(self, name):
        """Validate name: required, max 50 characters"""
        if not name or not isinstance(name, str):
            raise ValueError("Amenity name is required and must be a string")
        if len(name) > 50:
            raise ValueError("Amenity name must not exceed 50 characters")
        return name
