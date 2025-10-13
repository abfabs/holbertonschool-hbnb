from app.persistence.repository import InMemoryRepository
from app.models.user import User


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
    



    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass
