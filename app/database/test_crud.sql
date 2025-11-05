-- HBnB CRUD Testing Script
-- Use this script to manually test CRUD operations

-- ===== READ OPERATIONS =====
-- 1. Read all users
SELECT * FROM user;

-- 2. Read admin user
SELECT id, first_name, last_name, email, is_admin FROM user WHERE email = 'admin@hbnb.io';

-- 3. Read all amenities
SELECT id, name FROM amenity ORDER BY name;

-- 4. Count records in each table
SELECT 'user' as table_name, COUNT(*) as count FROM user
UNION ALL
SELECT 'amenity', COUNT(*) FROM amenity
UNION ALL
SELECT 'place', COUNT(*) FROM place
UNION ALL
SELECT 'review', COUNT(*) FROM review
UNION ALL
SELECT 'place_amenity', COUNT(*) FROM place_amenity;

-- ===== CREATE OPERATIONS (uncomment to test) =====
-- 1. Insert a new user
-- INSERT INTO user (id, first_name, last_name, email, password, is_admin)
-- VALUES (UUID(), 'John', 'Doe', 'john@example.com', 'hashedpassword123', FALSE);

-- 2. Insert a place (requires valid owner_id)
-- INSERT INTO place (id, title, description, price, latitude, longitude, owner_id)
-- VALUES (UUID(), 'Beautiful Beach House', 'A cozy beach house', 150.00, 40.7128, -74.0060, '36c9050e-ddd3-4c3b-9731-9f487208bbc1');

-- ===== UPDATE OPERATIONS (uncomment to test) =====
-- 1. Update user name
-- UPDATE user SET first_name = 'Jane' WHERE email = 'john@example.com';

-- 2. Update amenity name
-- UPDATE amenity SET name = 'High-Speed WiFi' WHERE name = 'WiFi';

-- ===== DELETE OPERATIONS (uncomment to test) =====
-- 1. Delete a user (be careful with foreign keys!)
-- DELETE FROM user WHERE email = 'john@example.com';

-- ===== CONSTRAINT TESTING =====
-- Try to create duplicate email (should fail)
-- INSERT INTO user (id, first_name, last_name, email, password, is_admin)
-- VALUES (UUID(), 'Another', 'User', 'admin@hbnb.io', 'password', FALSE);

-- Try to create review with rating out of range (should fail)
-- INSERT INTO review (id, text, rating, user_id, place_id)
-- VALUES (UUID(), 'Great place!', 10, 'user-id', 'place-id');

-- Try to create duplicate review for same user/place (should fail)
-- INSERT INTO review (id, text, rating, user_id, place_id)
-- VALUES (UUID(), 'Another review', 5, 'user-id', 'place-id');
