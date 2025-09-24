# HBnB Evolution - Airbnb Clone Project

## Objective
HBnB Evolution is a simplified Airbnb-like application designed to demonstrate modern web application architecture patterns. The project serves as a comprehensive learning platform for implementing layered architecture, business logic modeling, and API design while providing core vacation rental management functionality.

## Key Functionalities
- **User Management**: User registration, profile updates, and role-based access (regular users vs administrators)
- **Property Listings**: Create, update, and manage property listings with detailed descriptions, pricing, and location data
- **Review System**: Users can leave ratings and comments for properties they've visited
- **Amenity Management**: Comprehensive amenity catalog that can be associated with property listings
- **Audit Trail**: Automatic tracking of creation and modification timestamps for all entities

## Design
The application follows a strict three-layer architecture pattern:

### Architecture Layers
1. **Presentation Layer**: RESTful API endpoints handling client requests and responses
2. **Business Logic Layer**: Core application models (User, Place, Review, Amenity) and business rules enforcement
3. **Persistence Layer**: Database abstraction and data storage operations

### Core Entities
- **User**: First name, last name, email, password, admin status
- **Place**: Title, description, price, geolocation (latitude/longitude), owner association
- **Review**: Rating, comment, with relationships to both User and Place
- **Amenity**: Name and description, with many-to-many relationship to Places

### Technical Implementation
- **Unique Identification**: All entities feature UUID-based unique identifiers
- **Facade Pattern**: Inter-layer communication through simplified interfaces
- **UML Compliance**: Complete documentation using standardized UML notation
- **Database Agnostic**: Persistence layer designed for easy database implementation