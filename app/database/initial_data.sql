-- HBnB Initial Data Population Script

-- Insert Initial Amenities with UUID4 values
INSERT IGNORE INTO amenity (id, name, created_at, updated_at) VALUES
('550e8400-e29b-41d4-a716-446655440001', 'WiFi', NOW(), NOW()),
('550e8400-e29b-41d4-a716-446655440002', 'Swimming Pool', NOW(), NOW()),
('550e8400-e29b-41d4-a716-446655440003', 'Air Conditioning', NOW(), NOW()),
('550e8400-e29b-41d4-a716-446655440004', 'Kitchen', NOW(), NOW()),
('550e8400-e29b-41d4-a716-446655440005', 'Parking', NOW(), NOW()),
('550e8400-e29b-41d4-a716-446655440006', 'Pet Friendly', NOW(), NOW());

-- Insert Test Users (owners of the places)
INSERT IGNORE INTO user (id, email, first_name, last_name, password, is_admin, created_at, updated_at) VALUES
('650e8400-e29b-41d4-a716-446655440001', 'john.doe@example.com', 'John', 'Doe', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5aeJFqHFpjDKi', FALSE, NOW(), NOW()),
('650e8400-e29b-41d4-a716-446655440002', 'jane.smith@example.com', 'Jane', 'Smith', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5aeJFqHFpjDKi', FALSE, NOW(), NOW());

-- Insert Test Places with varying prices for filter testing
-- Schema: id, title, description, price, latitude, longitude, owner_id, created_at, updated_at
INSERT INTO place (id, title, description, price, latitude, longitude, owner_id, created_at, updated_at) VALUES
('750e8400-e29b-41d4-a716-446655440001', 'Cozy Studio Downtown', 'A small but cozy studio apartment in the heart of the city. Perfect for solo travelers.', 8.00, 41.3275, 19.8187, '650e8400-e29b-41d4-a716-446655440001', NOW(), NOW()),
('750e8400-e29b-41d4-a716-446655440002', 'Modern Apartment with WiFi', 'Spacious modern apartment with high-speed WiFi and comfortable workspace.', 35.00, 41.3275, 19.8187, '650e8400-e29b-41d4-a716-446655440001', NOW(), NOW()),
('750e8400-e29b-41d4-a716-446655440003', 'Charming Loft', 'Beautiful loft with exposed brick and city views. Walking distance to restaurants.', 45.00, 41.3245, 19.4531, '650e8400-e29b-41d4-a716-446655440002', NOW(), NOW()),
('750e8400-e29b-41d4-a716-446655440004', 'Seaside Villa', 'Stunning villa with direct beach access and swimming pool. Perfect for families.', 75.00, 40.4656, 19.4914, '650e8400-e29b-41d4-a716-446655440002', NOW(), NOW()),
('750e8400-e29b-41d4-a716-446655440005', 'Luxury Penthouse', 'High-end penthouse with panoramic city views and modern amenities.', 95.00, 41.3275, 19.8187, '650e8400-e29b-41d4-a716-446655440001', NOW(), NOW()),
('750e8400-e29b-41d4-a716-446655440006', 'Mountain Resort Chalet', 'Exclusive mountain resort with spa, restaurant, and breathtaking views.', 150.00, 42.0686, 19.5126, '650e8400-e29b-41d4-a716-446655440002', NOW(), NOW()),
('750e8400-e29b-41d4-a716-446655440007', 'Historic Mansion', 'Beautifully restored historic mansion with private garden and chef service.', 220.00, 40.7058, 19.9522, '650e8400-e29b-41d4-a716-446655440001', NOW(), NOW());

-- Link places to amenities
INSERT IGNORE INTO place_amenity (place_id, amenity_id) VALUES
('750e8400-e29b-41d4-a716-446655440001', '550e8400-e29b-41d4-a716-446655440001'),
('750e8400-e29b-41d4-a716-446655440002', '550e8400-e29b-41d4-a716-446655440001'),
('750e8400-e29b-41d4-a716-446655440002', '550e8400-e29b-41d4-a716-446655440003'),
('750e8400-e29b-41d4-a716-446655440003', '550e8400-e29b-41d4-a716-446655440001'),
('750e8400-e29b-41d4-a716-446655440004', '550e8400-e29b-41d4-a716-446655440001'),
('750e8400-e29b-41d4-a716-446655440004', '550e8400-e29b-41d4-a716-446655440002'),
('750e8400-e29b-41d4-a716-446655440005', '550e8400-e29b-41d4-a716-446655440001'),
('750e8400-e29b-41d4-a716-446655440006', '550e8400-e29b-41d4-a716-446655440001'),
('750e8400-e29b-41d4-a716-446655440006', '550e8400-e29b-41d4-a716-446655440002'),
('750e8400-e29b-41d4-a716-446655440007', '550e8400-e29b-41d4-a716-446655440001');
