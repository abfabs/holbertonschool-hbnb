![Logo](./images/hbnb_logo.jpg)

<h1 style="text-align:center;">HBnB Evolution - Airbnb Clone Project</h1>

## Table of Contents
- [Objective](#objective)
- [Project Status](#project-status)
- [Key Functionalities](#key-functionalities)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Frontend Implementation](#frontend-implementation)
- [API Documentation](#api-documentation)
- [Database Schema](#database-schema)
- [Package Diagram](#package-diagram)
- [Business Logic Diagram](#business-logic-diagram)
- [API Sequence Diagrams](#api-sequence-diagrams)
- [License](#license)
- [Authors](#authors)

---

<h2 style="text-align:center;">Objective</h2>

HBnB Evolution is an educational project that brings to life a simplified Airbnb-like platform. Users can register and manage their accounts, create and explore property listings with amenities, and submit reviews.

The project is designed to showcase:
- Modern web application architecture patterns
- Layered architecture (Presentation/API, Business Logic, Persistence)
- Best practices in modeling business logic
- API design and development
- A flexible persistence layer that works with MySQL databases

It highlights clear separation of concerns, audit tracking, and maintainable, scalable code, while giving hands-on experience in building a full-stack web application.

---

<h2 style="text-align:center;">Project Status</h2>

**Current Phase**: Full-Stack Application Complete ✅

**Backend:**
- ✅ REST API with Flask-RESTX fully implemented
- ✅ SQLAlchemy ORM with MySQL database integration
- ✅ Business logic layer with proper validation
- ✅ Authentication system (JWT tokens)
- ✅ Amenity management system
- ✅ Review system with ratings

**Frontend:**
- ✅ User authentication interface (Login page)
- ✅ Dynamic places listing with price filtering
- ✅ Detailed place view with amenities and reviews
- ✅ Interactive review submission form
- ✅ Responsive design with modern CSS

The application is production-ready with complete frontend-backend integration, CRUD operations, authentication, and error handling implemented.

---

<h2 style="text-align:center;">Key Functionalities</h2>

- **User Management**: Registration, profile updates, role-based access (users vs administrators)
- **Property Listings**: Create, update, manage listings with descriptions, pricing, and geolocation
- **Review System**: Rating (1-5 stars) and comment system for visited properties
- **Amenity Management**: Catalog system for property amenities with many-to-many relationships
- **Audit Trail**: Automatic creation/update timestamp tracking for all entities
- **Authentication**: JWT-based token authentication for secure API access
- **Authorization**: Role-based permissions (admin vs. regular users)
- **Interactive Frontend**: Responsive web interface with dynamic content loading

---

<h2 style="text-align:center;">Technology Stack</h2>

| Component | Technology |
|-----------|-----------|
| **Backend Framework** | Flask, Flask-RESTX |
| **Database** | MySQL 8.0+ |
| **ORM** | SQLAlchemy |
| **Authentication** | Flask-JWT-Extended (JWT tokens) |
| **Password Security** | bcrypt |
| **Language** | Python 3.x |
| **API Documentation** | Swagger/OpenAPI (via Flask-RESTX) |
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) |
| **Cross-Origin Support** | Flask-CORS |

---

<h2 style="text-align:center;">Project Structure</h2>

```
hbnb/
├── app/
│   ├── api/v1/                 # Presentation Layer - API endpoints
│   │   ├── users.py            # User endpoints
│   │   ├── places.py           # Place endpoints
│   │   ├── reviews.py          # Review endpoints
│   │   ├── amenities.py        # Amenity endpoints
│   │   └── auth.py             # Authentication endpoints
│   ├── models/                 # Data models
│   │   ├── basemodel.py        # Base model with common attributes
│   │   ├── user.py             # User model
│   │   ├── place.py            # Place model
│   │   ├── review.py           # Review model
│   │   ├── amenity.py          # Amenity model
│   │   └── placeamenity.py     # Many-to-many relationship
│   ├── services/               # Business Logic Layer
│   │   └── facade.py           # Facade pattern for business operations
│   ├── persistence/            # Persistence Layer
│   │   ├── repository.py       # Base repository classes
│   │   ├── userrepository.py   # User repository
│   │   ├── placerepository.py  # Place repository
│   │   ├── reviewrepository.py # Review repository
│   │   └── amenityrepository.py # Amenity repository
│   ├── database/               # Database setup and initialization
│   │   ├── schema.sql          # Database schema
│   │   ├── initialdata.sql     # Initial data
│   │   └── setupdatabase.py    # Setup script
│   ├── extensions.py           # Flask extensions (db, bcrypt, jwt)
│   └── __init__.py             # Flask app factory
├── front/                      # Frontend files
│   ├── index.html              # Main places listing page
│   ├── login.html              # User authentication page
│   ├── place.html              # Place details page
│   ├── addreview.html          # Review submission page (optional)
│   ├── styles.css              # Application styling
│   └── scripts.js              # Frontend JavaScript logic
├── images/                     # Application images and diagrams
├── config.py                   # Configuration settings
├── run.py                      # Application entry point
├── requirements.txt            # Python dependencies
└── README.md
```

### Three-Layer Architecture

**Presentation Layer** (`app/api/v1/`): REST API endpoints that receive requests and return formatted responses.

**Business Logic Layer** (`app/services/`): Core application logic, validation, and orchestration independent of any specific user interface or database technology.

**Persistence Layer** (`app/persistence/`): Database operations using SQLAlchemy, translating application objects into database records and vice versa.

---

<h2 style="text-align:center;">Installation & Setup</h2>

### Prerequisites

- Python 3.8 or higher
- MySQL 8.0 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, or Edge)

### Step 1: Clone the Repository

```bash
git clone https://github.com/abfabs/holbertonschool-hbnb.git
cd holbertonschool-hbnb
```

### Step 2: Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the root directory (or update `config.py`):
```
FLASK_ENV=development
FLASK_APP=run.py
DATABASE_URL=mysql+pymysql://root:password@localhost/hbnb_db
JWT_SECRET_KEY=your_secret_key_here
```

### Step 5: Set Up the Database
```bash
python app/database/setupdatabase.py
```

This will:
- Create the `hbnb_db` database
- Create all tables (user, place, review, amenity, placeamenity)
- Insert initial data (default amenities)

### Step 6: Run the Application
```bash
python run.py
```

The API will be available at `http://localhost:5000`  
Swagger API documentation: `http://localhost:5000/doc/`

### Step 7: Access the Frontend

Open your web browser and navigate to the frontend:
- **Home/Places Listing**: `http://localhost:5000/front/index.html` or serve via `python -m http.server 8000` from the `front/` directory
- **Login Page**: `http://localhost:5000/front/login.html`
- **Place Details**: Click "View Details" on any place card

---

<h2 style="text-align:center;">Frontend Implementation</h2>

### Overview

The frontend is built with vanilla HTML, CSS, and JavaScript, providing a responsive and interactive user experience. It communicates with the Flask backend API using JWT token-based authentication.

### Key Features

#### 1. User Authentication (Login)
- **Page**: `login.html`
- **Functionality**: Users can log in with their email and password to receive a JWT token stored in cookies
- **API Endpoint**: `POST /api/v1/auth/login`
- **Success**: Redirects to the places listing page with authentication enabled

#### 2. Places Listing
- **Page**: `index.html`
- **Features**:
  - Displays all available places dynamically fetched from the API
  - Price filtering dropdown (All, Up to $10, Up to $50, Up to $100)
  - Each place card shows title, price per night, and description preview
  - "View Details" button for each place
- **API Endpoint**: `GET /api/v1/places`
- **Authentication**: Optional for viewing, but login link is shown for unauthenticated users

#### 3. Place Details
- **Page**: `place.html?id={place_id}`
- **Features**:
  - Detailed place information (title, price, description, location coordinates, host name)
  - List of amenities associated with the place
  - All reviews with ratings, user names, and timestamps
  - Add review form (only visible for authenticated users)
- **API Endpoints**: 
  - `GET /api/v1/places/{place_id}` - Fetch place details
  - Reviews included in place response

#### 4. Review Submission
- **Component**: Review form on `place.html`
- **Features**:
  - Rating selection (1-5 stars)
  - Text review input
  - Form validation
  - Automatic page refresh after successful submission
- **API Endpoint**: `POST /api/v1/reviews`
- **Authentication**: Required (JWT token)

### Frontend Architecture

#### HTML Pages

**`login.html`**
- Simple login form with email and password fields
- Form submission handled by JavaScript
- Redirects to index page on success

**`index.html`**
- Header with logo and navigation (Home, Login/Logout button)
- Filter section for price-based filtering
- Dynamic places list populated via JavaScript
- Footer with copyright information

**`place.html`**
- Detailed place information section
- Amenities grid display
- Reviews section with individual review cards
- Conditional review submission form (authenticated users only)

#### CSS Styling (`styles.css`)

**Design Principles:**
- Clean, modern interface with consistent color scheme
- Primary brand color: `#5ec4b6` (teal)
- Responsive grid layouts for places and amenities
- Card-based design with hover effects
- Mobile-responsive with media queries for screens under 768px

**Key Style Components:**
- **Header**: Fixed navigation with logo and login button
- **Place Cards**: Grid layout with shadow effects and hover animations
- **Forms**: Consistent input styling with rounded corners
- **Buttons**: Primary action buttons in brand color with hover states
- **Reviews**: Card-based layout with user info and timestamps

#### JavaScript Logic (`scripts.js`)

**Core Functions:**

1. **Authentication Management**
   - `loginUser(email, password)`: Handles login API call and token storage
   - `checkAuthentication()`: Verifies token and adjusts UI accordingly
   - `setCookie()` / `getCookie()`: Cookie management for JWT tokens

2. **Places Operations**
   - `fetchPlaces(token)`: Retrieves all places from API
   - `displayPlaces(places)`: Dynamically renders place cards
   - `loadPriceFilter()`: Populates and manages price filter dropdown
   - `filterPlacesByPrice(maxPrice)`: Client-side filtering logic
   - `viewPlaceDetails(placeId)`: Navigation to place details page

3. **Place Details**
   - `getPlaceIdFromURL()`: Extracts place ID from query parameters
   - `fetchPlaceDetails(token, placeId)`: Retrieves detailed place information
   - `displayPlaceDetails(place)`: Renders place info, amenities, and reviews
   - `displayReviews(reviews)`: Creates review cards with ratings

4. **Review Submission**
   - `submitReview(token, placeId, rating, reviewText)`: Posts review to API
   - Form validation and error handling
   - Success feedback and page refresh

### API Integration

The frontend communicates with the backend using the Fetch API with the following pattern:

```javascript
// Example: Fetching places with authentication
const response = await fetch('http://127.0.0.1:5000/api/v1/places', {
    method: 'GET',
    headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
    }
});
```

**CORS Configuration**: The backend uses Flask-CORS to allow cross-origin requests from the frontend.

### User Experience Flow

1. **First-Time Visitor**:
   - Lands on `index.html` → sees all places
   - Can browse and filter places without logging in
   - Click "View Details" to see place information
   - Cannot submit reviews without authentication

2. **Authenticated User**:
   - Logs in via `login.html` → JWT token stored in cookies
   - Redirected to `index.html` → login button hidden
   - Can view place details with review form visible
   - Can submit reviews with ratings and text
   - Token automatically included in authenticated requests

### Responsive Design

The frontend is fully responsive with breakpoints at 768px:
- **Desktop**: Multi-column grid layouts for places and amenities
- **Mobile**: Single-column stacked layouts
- **Header**: Collapses navigation on smaller screens
- **Cards**: Full-width with adjusted padding

---

<h2 style="text-align:center;">API Documentation</h2>

### Authentication

All protected endpoints require a **Bearer Token** in the Authorization header:
```
Authorization: Bearer <your_jwt_token>
```

#### Login

- **Endpoint**: `POST /api/v1/auth/login`
- **Description**: Authenticate user and receive JWT token
- **Request Body**:
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```
- **Response** (200 OK):
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Users Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/v1/users` | Create new user (Admin only) | ✅ |
| GET | `/api/v1/users` | List all users | ✅ |
| GET | `/api/v1/users/<user_id>` | Get user details | ✅ |
| PUT | `/api/v1/users/<user_id>` | Update user | ✅ |

### Places Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/v1/places` | Create new place | ✅ |
| GET | `/api/v1/places` | List all places | ❌ |
| GET | `/api/v1/places/<place_id>` | Get place details | ❌ |
| PUT | `/api/v1/places/<place_id>` | Update place (owner only) | ✅ |
| DELETE | `/api/v1/places/<place_id>` | Delete place (owner only) | ✅ |

### Reviews Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/v1/reviews` | Submit new review | ✅ |
| GET | `/api/v1/reviews` | List all reviews | ❌ |
| GET | `/api/v1/reviews/<review_id>` | Get review details | ❌ |
| PUT | `/api/v1/reviews/<review_id>` | Update review (author only) | ✅ |
| DELETE | `/api/v1/reviews/<review_id>` | Delete review (author only) | ✅ |
| GET | `/api/v1/places/<place_id>/reviews` | List reviews for place | ❌ |

### Amenities Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/v1/amenities` | Create amenity (Admin only) | ✅ |
| GET | `/api/v1/amenities` | List all amenities | ❌ |
| GET | `/api/v1/amenities/<amenity_id>` | Get amenity details | ❌ |
| PUT | `/api/v1/amenities/<amenity_id>` | Update amenity (Admin only) | ✅ |

#### Example: Create a Place
```bash
curl -X POST http://localhost:5000/api/v1/places \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Beautiful Beach House",
    "description": "Cozy beachfront property with ocean view",
    "price": 150.00,
    "latitude": 40.7128,
    "longitude": -74.0060
  }'
```

---

<h2 style="text-align:center;">Database Schema</h2>

```mermaid
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
```

**Key Tables**:

- **user**: User accounts with authentication
- **place**: Property listings
- **review**: User reviews with ratings (1-5)
- **amenity**: Available amenities (WiFi, Pool, etc.)
- **placeamenity**: Many-to-many junction table linking places to amenities

**Constraints**:
- Email addresses must be unique
- Amenity names must be unique
- Ratings must be between 1-5
- One review per user per place

---

<h2 style="text-align:center;">Package Diagram</h2>

![High Level Package Diagram](./images/hl_package_diagram.jpg)

### Three-Layer Architecture

#### Presentation Layer
Provides the user interface and API contracts. It receives external requests, translates them into commands for the business layer, and returns formatted responses.

#### Business Logic Layer
The core of the application. It enforces business rules, processes data, and coordinates tasks. It is independent of any specific user interface or database technology.

#### Persistence Layer
Handles all data storage and retrieval. It translates application objects into database records and vice versa, insulating the business logic from database-specific details.

---

<h2 style="text-align:center;">Business Logic Diagram</h2>

![Business Logic Class Diagram](./images/business_logic_class_diagram.jpg)

### Class Responsibilities

**BaseModel**
- Attributes: `id` (UUID), `created_at`, `updated_at`
- Methods: Inherited by all classes

**User**
- Attributes: `first_name`, `last_name`, `email`, `password` (hashed), `is_admin`
- Methods: register, update, delete, list, list_all_places

**Place**
- Attributes: `owner_id`, `title`, `description`, `price`, `latitude`, `longitude`, `amenities`
- Methods: create, update, delete, list_place(s), list_all_places

**Review**
- Attributes: `owner_id`, `place_id`, `rating`, `comment`
- Methods: create, update, delete, list_review(s)

**Amenities**
- Attributes: `name`, `description`
- Methods: create, delete, list_amenity, list_all_amenities

---

<h2 style="text-align:center;">API Sequence Diagrams</h2>

### User Registration Flow
![User Registration Flow](./images/user_creation_flow.png)

#### User Registration Summary
1. **Client → API Service**: `POST /users/register {username, email, password}`
2. **Validation (API Service)**: Invalid/missing fields → **400 Bad Request** or Valid → continue
3. **Check User (Business Logic → DB)**: Exists → **409 Conflict** or Not exists → continue
4. **Create User (Business Logic)**: Hash password, create user instance, save to DB
5. **Save Result (DB)**: Error → **500 Internal Server Error** or Success → **201 Created + user details**

**Code Legend**: **400** = Bad input, **409** = Duplicate user, **500** = DB error, **201** = User created, Password is always **hashed** before saving

### Place Creation Flow
![Place Creation Flow](./images/place_creation_flow.png)

#### Place Creation Summary
1. **Client Request**: `POST /places` with authentication token and place data
2. **Authentication**: Token verified by **Auth Service**, Invalid/expired → **401 Unauthorized**
3. **Validation**: Place data checked, Invalid → **400 Bad Request**
4. **Authorization**: User permissions verified, Unauthorized → **403 Forbidden**
5. **Place Creation**: Instance created and persisted, DB error → **500 Internal Server Error**
6. **Response**: Success → **201 Created** with place details

**Code Legend**: **400** = Bad input, **401** = Unauthorized, **403** = Forbidden, **500** = DB error, **201** = Place created

### Review Submission Flow
![Review Submission Flow](./images/review%20flow.png)

#### Review Submission Summary
1. **Validation**: Check if **User** and **Place** exist, If missing → **404 Not Found**
2. **Input Checking**: Validate `rating` and `comment` fields, Invalid → **400 Bad Request**
3. **Review Creation**: New review instance created
4. **Persistence Layer**: Saves to database, Error → **500 Internal Server Error**
5. **Response**: Success → **201 Created** with review details

**Code Legend**: **400** = Bad input, **404** = User or Place not found, **500** = DB error, **201** = Review created

### Fetching Places Flow
![Fetching Places Flow](./images/fetching_places_flow.png)

#### Fetching Places Summary
1. **Input Validation**: Filters checked before querying DB
2. **Error Handling**: Invalid → **400 Bad Request**, No data → **200 OK** with empty list, DB error → **500 Internal Server Error**, Success → **200 OK** with results
3. **Layered Responsibility**: **Presentation Layer** = Validation & formatting, **Business Logic Layer** = Processing & orchestration, **Persistence Layer** = Raw data retrieval/storage

**Code Legend**: **400** = Bad input, **500** = DB error, **200** = OK (with results or empty list)

---

<h2 align="center">License</h2>

This project is for educational purposes only and is part of the **Holberton School** / **Foundations of Computer Science** curriculum.

---

<h2 align="center">Authors</h2>

<p>
  <strong>Alba Eftimi</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <strong>Sokol Gjeka</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <strong>Renis Vukaj</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <strong>Kevin Voka</strong>

  GitHub: <a href="https://github.com/abfabs">abfabs</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  GitHub: <a href="https://github.com/sokolgj19">sokolgj19</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  GitHub: <a href="https://github.com/renisv">renisv</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  GitHub: <a href="https://github.com/kevin10v">kevin10v</a>
</p>

<p align="center">
  <em>November 2025</em><br>
  <em>Tirana, Albania</em>
</p>
