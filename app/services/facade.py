from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review


class HBnBFacade:
    # Initialize the facade with in-memory repositories for all entities
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()


    # Method for creating a user
    def create_user(self, user_data):
        user_exists = self.get_user_by_email(user_data.get('email'))
        if user_exists: 
            raise ValueError("User already exists")
        
        user = User(**user_data)
        self.user_repo.add(user)
        return user


    # Retrieve a user by their unique identifier
    def get_user(self, user_id):
        return self.user_repo.get(user_id)


    # Retrieve a user by their email address
    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
    
    # Retrieve all users from the repository
    def get_all_users(self):
        return self.user_repo.get_all()
    
    # Update user information after validating email uniqueness if changed
    def update_user(self, user_id, user_data):
        user = self.get_user(user_id)
        if not user:
            return None
        
        if 'email' in user_data and user_data['email'] != user.email:
            user_exists = self.get_user_by_email(user_data['email'])
            if user_exists:
                raise ValueError("Email already registered")
            
        self.user_repo.update(user_id, user_data)
        return user
    

    def create_amenity(self, amenity_data):
        amenity_name = amenity_data.get("name")

        if not amenity_name:
            raise ValueError("Amenity name is required")

        existing_amenities = self.amenity_repo.get_all()
        for amenity in existing_amenities:
            if amenity.name.lower() == amenity_name.lower():
                raise ValueError(f"Amenity with name '{amenity_name}' already exists")

        amenity = Amenity(name=amenity_name)
        self.amenity_repo.add(amenity)
        return amenity

    
    def get_all_amenities(self):
        return self.amenity_repo.get_all()
    
    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)
    
    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            return None

        new_name = amenity_data.get("name")
        if new_name:
            existing_amenities = self.amenity_repo.get_all()
            for other_amenity in existing_amenities:
                if other_amenity.name.lower() == new_name.lower():
                    raise ValueError(f"Amenity with name '{new_name}' already exists")

        self.amenity_repo.update(amenity_id, amenity_data)
        return amenity


    def create_place(self, place_data):
        """Create a new place with validation"""
        # Validate required fields
        owner_id = place_data.get('owner_id')
        if not owner_id:
            raise ValueError("Owner ID is required")
        
        # Verify that the owner exists
        owner = self.get_user(owner_id)
        if not owner:
            raise ValueError("Owner not found")
        
        # Extract place data
        title = place_data.get('title')
        description = place_data.get('description', '')
        price = place_data.get('price')
        latitude = place_data.get('latitude')
        longitude = place_data.get('longitude')
        
        # Create the place instance (validation happens in Place.__init__)
        place = Place(
            title=title,
            description=description,
            price=price,
            latitude=latitude,
            longitude=longitude,
            owner=owner
        )
        
        # Add to repository
        self.place_repo.add(place)
        
        return place


    def get_place(self, place_id):
        """Retrieve a place by its unique identifier"""
        return self.place_repo.get(place_id)

    def get_all_places(self):
        """Retrieve all places from the repository"""
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        """Update place information after validating owner if changed"""
        place = self.get_place(place_id)
        if not place:
            return None
        
        # If owner_id is being updated, verify the new owner exists
        if 'owner_id' in place_data:
            new_owner = self.get_user(place_data['owner_id'])
            if not new_owner:
                raise ValueError("Owner not found")
            # Replace owner_id with actual owner object for validation
            place_data['owner'] = new_owner
            del place_data['owner_id']
        
        self.place_repo.update(place_id, place_data)
        return place
    


    def create_review(self, review_data):
        """Create a new review with validation for user, place, and rating"""
        # Validate required fields
        user_id = review_data.get('user_id')
        place_id = review_data.get('place_id')
        
        if not user_id:
            raise ValueError("User ID is required")
        if not place_id:
            raise ValueError("Place ID is required")
        
        # Verify that the user exists
        user = self.get_user(user_id)
        if not user:
            raise ValueError("User not found")
        
        # Verify that the place exists
        place = self.get_place(place_id)
        if not place:
            raise ValueError("Place not found")
        
        # NEW: Check if user is trying to review their own place
        if place.owner.id == user_id:
            raise ValueError("You cannot review your own place")
        
        # NEW: Check if user has already reviewed this place
        existing_reviews = self.get_reviews_by_place(place_id)
        for review in existing_reviews:
            if review.user.id == user_id:
                raise ValueError("You have already reviewed this place")
        
        # Extract review data
        text = review_data.get('text')
        rating = review_data.get('rating')
        
        # Create the review instance (validation happens in Review.__init__)
        review = Review(
            text=text,
            rating=rating,
            place=place,
            user=user
        )
        
        # Add review to repository
        self.review_repo.add(review)
        
        # Add review to the place's review list
        place.add_review(review)
        
        return review


    def get_review(self, review_id):
        """Retrieve a review by its unique identifier"""
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        """Retrieve all reviews from the repository"""
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        """Retrieve all reviews for a specific place"""
        place = self.get_place(place_id)
        if not place:
            return None
        return place.reviews

    def update_review(self, review_id, review_data):
        """Update review info after validating user and place if changed"""
        review = self.get_review(review_id)
        if not review:
            return None
        
        # NEW: Validate rating if it's being updated
        if 'rating' in review_data:
            rating = review_data['rating']
            if not isinstance(rating, int) or rating < 1 or rating > 5:
                raise ValueError("Rating must be between 1 and 5")
        
        # If user_id is being updated, verify the new user exists
        if 'user_id' in review_data:
            new_user = self.get_user(review_data['user_id'])
            if not new_user:
                raise ValueError("User not found")
            review_data['user'] = new_user
            del review_data['user_id']
        
        # If place_id is being updated, verify the new place exists
        if 'place_id' in review_data:
            new_place = self.get_place(review_data['place_id'])
            if not new_place:
                raise ValueError("Place not found")
            review_data['place'] = new_place
            del review_data['place_id']
        
        self.review_repo.update(review_id, review_data)
        return review


    def delete_review(self, review_id):
        """Delete a review from the repository"""
        review = self.get_review(review_id)
        if not review:
            return False
        
        # Remove review from the place's review list
        if review.place and review in review.place.reviews:
            review.place.reviews.remove(review)
        
        self.review_repo.delete(review_id)
        return True