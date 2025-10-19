from app.models.base_model import BaseModel


class Review(BaseModel):
    # Initialize a new review with validated attributes
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = self.validate_text(text)
        self.rating = self.validate_rating(rating)
        self.place = self.validate_place(place)
        self.user = self.validate_user(user)


    # Validate that the review text is a non-empty string
    def validate_text(self, text):
        """Validate text: required"""
        if not text or not isinstance(text, str):
            raise ValueError("Review text is required and must be a string")
        return text


    # Validate that the rating is an integer between 1 and 5
    def validate_rating(self, rating):
        """Validate rating: must be between 1 and 5"""
        if not isinstance(rating, int):
            raise ValueError("Rating must be an integer")
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
        return rating


    # Validate that the place is a valid Place instance
    def validate_place(self, place):
        """Validate place: must be a Place instance"""
        from app.models.place import Place
        if not isinstance(place, Place):
            raise ValueError("Place must be a valid Place instance")
        return place


    # Validate that the user is a valid User instance
    def validate_user(self, user):
        """Validate user: must be a User instance"""
        from app.models.user import User
        if not isinstance(user, User):
            raise ValueError("User must be a valid User instance")
        return user
    
    # NEW METHOD: Override update to re-validate rating
    def update(self, data):
        """Update the attributes with validation"""
        for key, value in data.items():
            if hasattr(self, key):
                # Validate rating if it's being updated
                if key == 'rating':
                    value = self.validate_rating(value)
                elif key == 'text':
                    value = self.validate_text(value)
                setattr(self, key, value)
        self.save()