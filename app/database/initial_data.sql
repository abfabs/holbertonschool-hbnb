-- HBnB Initial Data Population Script


-- Insert Initial Amenities with UUID4 values
INSERT INTO amenity (id, name, created_at, updated_at) VALUES
('550e8400-e29b-41d4-a716-446655440001', 'WiFi', NOW(), NOW()),
('550e8400-e29b-41d4-a716-446655440002', 'Swimming Pool', NOW(), NOW()),
('550e8400-e29b-41d4-a716-446655440003', 'Air Conditioning', NOW(), NOW());
