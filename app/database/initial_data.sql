-- HBnB Initial Data Population Script
-- This script inserts the admin user and initial amenities

-- Insert Administrator User
INSERT INTO user (id, first_name, last_name, email, password, is_admin) 
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
    'Admin',
    'HBnB',
    'admin@hbnb.io',
    '$2b$12$eIst8jHXP4nhGHERe6ZP..Z1VJLVMfL7F8qKCvyp.WJqpf1NW4BKe',
    TRUE
);

-- Insert Initial Amenities with UUID4 values
INSERT INTO amenity (id, name) VALUES
('550e8400-e29b-41d4-a716-446655440001', 'WiFi'),
('550e8400-e29b-41d4-a716-446655440002', 'Swimming Pool'),
('550e8400-e29b-41d4-a716-446655440003', 'Air Conditioning');
