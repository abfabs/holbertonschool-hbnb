from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

def test_user_creation():
    """Test User class creation and validation"""
    print("\n--- Testing User Creation ---")
    try:
        user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
        assert user.first_name == "John"
        assert user.last_name == "Doe"
        assert user.email == "john.doe@example.com"
        assert user.is_admin is False
        assert user.id is not None
        assert user.created_at is not None
        print("✓ User creation test passed!")
    except AssertionError as e:
        print(f"✗ User creation test failed: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

def test_user_validation():
    """Test User validation"""
    print("\n--- Testing User Validation ---")
    # Test invalid email
    try:
        user = User(first_name="John", last_name="Doe", email="invalid-email")
        print("✗ Should have raised ValueError for invalid email")
    except ValueError:
        print("✓ Invalid email validation passed!")

    # Test missing first name
    try:
        user = User(first_name="", last_name="Doe", email="john@example.com")
        print("✗ Should have raised ValueError for empty first name")
    except ValueError:
        print("✓ Empty first name validation passed!")

def test_amenity_creation():
    """Test Amenity class creation"""
    print("\n--- Testing Amenity Creation ---")
    try:
        amenity = Amenity(name="Wi-Fi")
        assert amenity.name == "Wi-Fi"
        assert amenity.id is not None
        print("✓ Amenity creation test passed!")
    except AssertionError as e:
        print(f"✗ Amenity creation test failed: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

def test_place_creation():
    """Test Place class creation with relationships"""
    print("\n--- Testing Place Creation ---")
    try:
        owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com")
        place = Place(
            title="Cozy Apartment",
            description="A nice place to stay",
            price=100.0,
            latitude=37.7749,
            longitude=-122.4194,
            owner=owner
        )
        
        assert place.title == "Cozy Apartment"
        assert place.price == 100.0
        assert place.latitude == 37.7749
        assert place.longitude == -122.4194
        assert place.owner == owner
        assert len(place.reviews) == 0
        assert len(place.amenities) == 0
        print("✓ Place creation test passed!")
    except AssertionError as e:
        print(f"✗ Place creation test failed: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

def test_place_validation():
    """Test Place validation"""
    print("\n--- Testing Place Validation ---")
    owner = User(first_name="Alice", last_name="Smith", email="alice@example.com")
    
    # Test invalid price
    try:
        place = Place(title="Test", description="", price=-10, latitude=0, longitude=0, owner=owner)
        print("✗ Should have raised ValueError for negative price")
    except ValueError:
        print("✓ Negative price validation passed!")
    
    # Test invalid latitude
    try:
        place = Place(title="Test", description="", price=100, latitude=100, longitude=0, owner=owner)
        print("✗ Should have raised ValueError for invalid latitude")
    except ValueError:
        print("✓ Invalid latitude validation passed!")

def test_review_creation():
    """Test Review class creation with relationships"""
    print("\n--- Testing Review Creation ---")
    try:
        owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com")
        place = Place(
            title="Cozy Apartment",
            description="A nice place to stay",
            price=100.0,
            latitude=37.7749,
            longitude=-122.4194,
            owner=owner
        )
        
        review = Review(text="Great stay!", rating=5, place=place, user=owner)
        place.add_review(review)
        
        assert review.text == "Great stay!"
        assert review.rating == 5
        assert review.place == place
        assert review.user == owner
        assert len(place.reviews) == 1
        assert place.reviews[0] == review
        print("✓ Review creation and relationship test passed!")
    except AssertionError as e:
        print(f"✗ Review creation test failed: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

def test_review_validation():
    """Test Review validation"""
    print("\n--- Testing Review Validation ---")
    owner = User(first_name="Alice", last_name="Smith", email="alice@example.com")
    place = Place(title="Test", description="", price=100, latitude=0, longitude=0, owner=owner)
    
    # Test invalid rating
    try:
        review = Review(text="Good", rating=6, place=place, user=owner)
        print("✗ Should have raised ValueError for rating > 5")
    except ValueError:
        print("✓ Invalid rating validation passed!")

def test_place_amenity_relationship():
    """Test Place-Amenity many-to-many relationship"""
    print("\n--- Testing Place-Amenity Relationship ---")
    try:
        owner = User(first_name="Bob", last_name="Builder", email="bob@example.com")
        place = Place(title="Modern Loft", description="", price=150, latitude=0, longitude=0, owner=owner)
        
        wifi = Amenity(name="Wi-Fi")
        parking = Amenity(name="Parking")
        
        place.add_amenity(wifi)
        place.add_amenity(parking)
        
        assert len(place.amenities) == 2
        assert wifi in place.amenities
        assert parking in place.amenities
        print("✓ Place-Amenity relationship test passed!")
    except AssertionError as e:
        print(f"✗ Place-Amenity relationship test failed: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

def test_update_method():
    """Test the update method from BaseModel"""
    print("\n--- Testing Update Method ---")
    try:
        user = User(first_name="John", last_name="Doe", email="john@example.com")
        original_updated_at = user.updated_at
        
        import time
        time.sleep(0.01)  # Small delay to ensure timestamp difference
        
        user.update({"first_name": "Jane", "last_name": "Smith"})
        
        assert user.first_name == "Jane"
        assert user.last_name == "Smith"
        assert user.updated_at > original_updated_at
        print("✓ Update method test passed!")
    except AssertionError as e:
        print(f"✗ Update method test failed: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

# Run all tests
if __name__ == "__main__":
    print("=" * 50)
    print("Running Business Logic Layer Tests")
    print("=" * 50)
    
    test_user_creation()
    test_user_validation()
    test_amenity_creation()
    test_place_creation()
    test_place_validation()
    test_review_creation()
    test_review_validation()
    test_place_amenity_relationship()
    test_update_method()
    
    print("\n" + "=" * 50)
    print("All tests completed!")
    print("=" * 50)
