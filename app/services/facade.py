from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.persistence.repository import UserRepository, PlaceRepository, ReviewRepository, AmenityRepository
from app.extensions import db

class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()
        self.place_repo = PlaceRepository()
        self.review_repo = ReviewRepository()
        self.amenity_repo = AmenityRepository()
    
    # ========== USER METHODS ==========
    def create_user(self, first_name, last_name, email, is_admin=False):
        """Create a new user"""
        user = User(first_name=first_name, last_name=last_name, email=email, is_admin=is_admin)
        return self.user_repo.add(user)
    
    def get_user(self, user_id):
        """Get a user by ID"""
        return self.user_repo.get(user_id)
    
    def get_all_users(self):
        """Get all users"""
        return self.user_repo.get_all()
    
    def update_user(self, user_id, first_name=None, last_name=None, email=None, is_admin=None):
        """Update a user"""
        user = self.user_repo.get(user_id)
        if not user:
            return None
        if first_name:
            user.first_name = user.validate_first_name(first_name)
        if last_name:
            user.last_name = user.validate_last_name(last_name)
        if email:
            user.email = user.validate_email(email)
        if is_admin is not None:
            user.is_admin = is_admin
        return self.user_repo.update(user)
    
    def delete_user(self, user_id):
        """Delete a user"""
        return self.user_repo.delete(user_id)
    
    # ========== PLACE METHODS ==========
    def create_place(self, title, description, price, latitude, longitude, owner_id):
        """Create a new place"""
        place = Place(
            title=title,
            description=description,
            price=price,
            latitude=latitude,
            longitude=longitude,
            owner_id=owner_id
        )
        return self.place_repo.add(place)
    
    def get_place(self, place_id):
        """Get a place by ID"""
        return self.place_repo.get(place_id)
    
    def get_all_places(self):
        """Get all places"""
        return self.place_repo.get_all()
    
    def update_place(self, place_id, title=None, description=None, price=None, latitude=None, longitude=None):
        """Update a place"""
        place = self.place_repo.get(place_id)
        if not place:
            return None
        if title:
            place.title = place.validate_title(title)
        if description:
            place.description = description
        if price:
            place.price = place.validate_price(price)
        if latitude:
            place.latitude = place.validate_latitude(latitude)
        if longitude:
            place.longitude = place.validate_longitude(longitude)
        return self.place_repo.update(place)
    
    def delete_place(self, place_id):
        """Delete a place"""
        return self.place_repo.delete(place_id)
    
    def get_places_by_owner(self, owner_id):
        """Get all places owned by a user"""
        user = self.user_repo.get(owner_id)
        if not user:
            return []
        return user.places
    
    def add_amenity_to_place(self, place_id, amenity_id):
        """Add an amenity to a place"""
        place = self.place_repo.get(place_id)
        amenity = self.amenity_repo.get(amenity_id)
        if place and amenity:
            place.amenities.append(amenity)
            self.place_repo.update(place)
            return place
        return None
    
    def remove_amenity_from_place(self, place_id, amenity_id):
        """Remove an amenity from a place"""
        place = self.place_repo.get(place_id)
        amenity = self.amenity_repo.get(amenity_id)
        if place and amenity and amenity in place.amenities:
            place.amenities.remove(amenity)
            self.place_repo.update(place)
            return place
        return None
    
    # ========== REVIEW METHODS ==========
    def create_review(self, text, rating, user_id, place_id):
        """Create a new review"""
        review = Review(
            text=text,
            rating=rating,
            user_id=user_id,
            place_id=place_id
        )
        return self.review_repo.add(review)
    
    def get_review(self, review_id):
        """Get a review by ID"""
        return self.review_repo.get(review_id)
    
    def get_all_reviews(self):
        """Get all reviews"""
        return self.review_repo.get_all()
    
    def update_review(self, review_id, text=None, rating=None):
        """Update a review"""
        review = self.review_repo.get(review_id)
        if not review:
            return None
        if text:
            review.text = review.validate_text(text)
        if rating:
            review.rating = review.validate_rating(rating)
        return self.review_repo.update(review)
    
    def delete_review(self, review_id):
        """Delete a review"""
        return self.review_repo.delete(review_id)
    
    def get_reviews_by_place(self, place_id):
        """Get all reviews for a place"""
        place = self.place_repo.get(place_id)
        if not place:
            return []
        return place.reviews
    
    def get_reviews_by_user(self, user_id):
        """Get all reviews written by a user"""
        user = self.user_repo.get(user_id)
        if not user:
            return []
        return user.reviews
    
    # ========== AMENITY METHODS ==========
    def create_amenity(self, name):
        """Create a new amenity"""
        amenity = Amenity(name=name)
        return self.amenity_repo.add(amenity)
    
    def get_amenity(self, amenity_id):
        """Get an amenity by ID"""
        return self.amenity_repo.get(amenity_id)
    
    def get_all_amenities(self):
        """Get all amenities"""
        return self.amenity_repo.get_all()
    
    def update_amenity(self, amenity_id, name=None):
        """Update an amenity"""
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return None
        if name:
            amenity.name = amenity.validate_name(name)
        return self.amenity_repo.update(amenity)
    
    def delete_amenity(self, amenity_id):
        """Delete an amenity"""
        return self.amenity_repo.delete(amenity_id)
