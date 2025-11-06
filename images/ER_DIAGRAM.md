# HBnB Database ER Diagram

## Entity-Relationship Diagram

This diagram represents the database schema for the HBnB (Holberton Airbnb Clone) project.

erDiagram
USER ||--o{ PLACE : "owns"
USER ||--o{ REVIEW : "writes"
PLACE ||--o{ REVIEW : "receives"
PLACE }o--|| AMENITY : "has"

USER {
    string id PK "UUID"
    string first_name
    string last_name
    string email UK "Unique"
    string password
    boolean is_admin
    datetime created_at
    datetime updated_at
}

PLACE {
    string id PK "UUID"
    string title
    string description
    float price
    float latitude
    float longitude
    string owner_id FK "references USER.id"
    datetime created_at
    datetime updated_at
}

REVIEW {
    string id PK "UUID"
    string text
    int rating "1-5"
    string user_id FK "references USER.id"
    string place_id FK "references PLACE.id"
    datetime created_at
    datetime updated_at
}

AMENITY {
    string id PK "UUID"
    string name UK "Unique"
    datetime created_at
    datetime updated_at
}

PLACE_AMENITY {
    string place_id FK "references PLACE.id"
    string amenity_id FK "references AMENITY.id"
    datetime created_at
}


## Relationships Summary

| Relationship | Type | Details |
|-------------|------|---------|
| USER → PLACE | One-to-Many | One user owns many places |
| USER → REVIEW | One-to-Many | One user writes many reviews |
| PLACE → REVIEW | One-to-Many | One place receives many reviews |
| PLACE ↔ AMENITY | Many-to-Many | Places have many amenities via PLACE_AMENITY |

## Constraint Details

- **USER.email**: UNIQUE - No duplicate emails allowed
- **AMENITY.name**: UNIQUE - No duplicate amenity names
- **REVIEW.rating**: CHECK (1-5) - Ratings must be between 1 and 5
- **REVIEW**: UNIQUE(user_id, place_id) - One review per user per place

## Key Points

1. **Primary Keys (PK)**: All tables use UUID as primary key
2. **Foreign Keys (FK)**:
   - `PLACE.owner_id` references `USER.id`
   - `REVIEW.user_id` references `USER.id`
   - `REVIEW.place_id` references `PLACE.id`
   - `PLACE_AMENITY.place_id` references `PLACE.id`
   - `PLACE_AMENITY.amenity_id` references `AMENITY.id`
3. **Cascading Deletes**: Enabled for all relationships to maintain referential integrity

## Database Schema Version

- **Last Updated**: November 5, 2025
- **Authors**: Holberton C27 Tirana  



