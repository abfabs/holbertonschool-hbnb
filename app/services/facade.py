from app.persistence.repository import InMemoryRepository
from app.persistence.user_repository import UserRepository
from app.persistence.place_repository import PlaceRepository
from app.persistence.review_repository import ReviewRepository
from app.persistence.amenity_repository import AmenityRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review


class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()
        self.place_repo = PlaceRepository()
        self.review_repo = ReviewRepository()
        self.amenity_repo = AmenityRepository()

    # ==================== USER METHODS ====================
    def create_user(self, user_data):
        """Create a new user with hashed password"""
        user_exists = self.get_user_by_email(user_data.get('email'))
        if user_exists:
            raise ValueError("User already exists")
        
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """Retrieve a user by ID"""
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """Retrieve a user by email"""
        return self.user_repo.get_user_by_email(email)

    def get_all_users(self):
        """Retrieve all users"""
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        """Update user information"""
        user = self.get_user(user_id)
        if not user:
            return None
        
        if 'email' in user_data and user_data['email'] != user.email:
            user_exists = self.get_user_by_email(user_data['email'])
            if user_exists:
                raise ValueError("Email already registered")
        
        if 'password' in user_data:
            user.hash_password(user_data['password'])
            del user_data['password']
        
        self.user_repo.update(user_id, user_data)
        return user

    # ==================== AMENITY METHODS ====================
    def create_amenity(self, amenity_data):
        """Create a new amenity"""
        amenity_name = amenity_data.get('name')
        if not amenity_name:
            raise ValueError("Amenity name is required")
        
        existing_amenities = self.get_all_amenities()
        for amenity in existing_amenities:
            if amenity.name.lower() == amenity_name.lower():
                raise ValueError(f"Amenity with name {amenity_name} already exists")
        
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_all_amenities(self):
        """Retrieve all amenities"""
        return self.amenity_repo.get_all()

    def get_amenity(self, amenity_id):
        """Retrieve an amenity by ID"""
        return self.amenity_repo.get(amenity_id)

    def update_amenity(self, amenity_id, amenity_data):
        """Update an amenity"""
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            return None
        
        new_name = amenity_data.get('name')
        if new_name:
            existing_amenities = self.get_all_amenities()
            for other_amenity in existing_amenities:
                if other_amenity.name.lower() == new_name.lower() and other_amenity.id != amenity_id:
                    raise ValueError(f"Amenity with name {new_name} already exists")
        
        self.amenity_repo.update(amenity_id, amenity_data)
        return amenity

    # ==================== PLACE METHODS ====================
    def create_place(self, place_data):
        """Create a new place"""
        owner_id = place_data.get('owner_id')
        if not owner_id:
            raise ValueError("Owner ID is required")
        
        owner = self.get_user(owner_id)
        if not owner:
            raise ValueError("Owner not found")
        
        title = place_data.get('title')
        description = place_data.get('description', '')
        price = place_data.get('price')
        latitude = place_data.get('latitude')
        longitude = place_data.get('longitude')
        
        place = Place(
            title=title,
            description=description,
            price=price,
            latitude=latitude,
            longitude=longitude,
            owner=owner
        )
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        """Retrieve a place by ID"""
        return self.place_repo.get(place_id)

    def get_all_places(self):
        """Retrieve all places"""
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        """Update a place"""
        place = self.get_place(place_id)
        if not place:
            return None
        
        if 'owner_id' in place_data:
            new_owner = self.get_user(place_data['owner_id'])
            if not new_owner:
                raise ValueError("Owner not found")
            place_data['owner'] = new_owner
            del place_data['owner_id']
        
        self.place_repo.update(place_id, place_data)
        return place

    def delete_place(self, place_id):
        """Delete a place"""
        place = self.get_place(place_id)
        if not place:
            return False
        
        self.place_repo.delete(place_id)
        return True

    # ==================== REVIEW METHODS ====================
    def create_review(self, review_data):
        """Create a new review"""
        user_id = review_data.get('user_id')
        place_id = review_data.get('place_id')
        
        if not user_id:
            raise ValueError("User ID is required")
        if not place_id:
            raise ValueError("Place ID is required")
        
        user = self.get_user(user_id)
        if not user:
            raise ValueError("User not found")
        
        place = self.get_place(place_id)
        if not place:
            raise ValueError("Place not found")
        
        if place.owner.id == user_id:
            raise ValueError("You cannot review your own place")
        
        existing_reviews = self.get_reviews_by_place(place_id)
        if existing_reviews:
            for review in existing_reviews:
                if review.user.id == user_id:
                    raise ValueError("You have already reviewed this place")
        
        text = review_data.get('text')
        rating = review_data.get('rating')
        
        review = Review(
            text=text,
            rating=rating,
            place=place,
            user=user
        )
        self.review_repo.add(review)
        place.add_review(review)
        return review

    def get_review(self, review_id):
        """Retrieve a review by ID"""
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        """Retrieve all reviews"""
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        """Retrieve all reviews for a specific place"""
        place = self.get_place(place_id)
        if not place:
            return None
        return place.reviews

    def update_review(self, review_id, review_data):
        """Update a review"""
        review = self.get_review(review_id)
        if not review:
            return None
        
        if 'rating' in review_data:
            rating = review_data['rating']
            if not isinstance(rating, int) or rating < 1 or rating > 5:
                raise ValueError("Rating must be between 1 and 5")
        
        if 'user_id' in review_data:
            new_user = self.get_user(review_data['user_id'])
            if not new_user:
                raise ValueError("User not found")
            review_data['user'] = new_user
            del review_data['user_id']
        
        if 'place_id' in review_data:
            new_place = self.get_place(review_data['place_id'])
            if not new_place:
                raise ValueError("Place not found")
            review_data['place'] = new_place
            del review_data['place_id']
        
        self.review_repo.update(review_id, review_data)
        return review

    def delete_review(self, review_id):
        """Delete a review"""
        review = self.get_review(review_id)
        if not review:
            return False
        
        if review.place and review in review.place.reviews:
            review.place.reviews.remove(review)
        
        self.review_repo.delete(review_id)
        return True
