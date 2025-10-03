![Logo](./images/hbnb_logo.jpg)

# HBnB Evolution - Airbnb Clone Project

## Table of Contents
- [Objective](#objective)
- [Key Functionalities](#key-functionalities)
- [Package Diagram](#package-diagram)
- [Business Logic Diagram](#business-logic-diagram)
- [API Sequence Diagrams](#api-sequence-diagrams)
  - [User Registration Flow](#user-registration-flow)
  - [Place Creation Flow](#place-creation-flow)
  - [Review Submission Flow](#review-submission-flow)
  - [Fetching Places Flow](#fetching-places-flow)
- [License](#license)
- [Authors](#authors)

---

## Objective

HBnB Evolution is an educational project that brings to life a simplified Airbnb-like platform. Users can register and manage their accounts, create and explore property listings with amenities, and submit reviews. 

The project is designed to showcase:

- Modern web application architecture patterns  
- Layered architecture (Presentation/API, Business Logic, Persistence)  
- Best practices in modeling business logic  
- API design and development  
- A flexible persistence layer that can work with different databases  

It highlights clear separation of concerns, audit tracking, and maintainable, scalable code, while giving hands-on experience in building a full-stack web application.

---

## Key Functionalities

- **User Management**: Registration, profile updates, role-based access (users vs administrators)
- **Property Listings**: Create, update, manage listings with descriptions, pricing, and geolocation
- **Review System**: Rating and comment system for visited properties
- **Amenity Management**: Catalog system for property amenities with many-to-many relationships
- **Audit Trail**: Automatic creation/update timestamp tracking for all entities

---

## Package Diagram

![High Level Package Diagram](./images/hl_package_diagram.jpg)

### Three-Layer Architecture

#### Presentation Layer
- Provides the user interface and API contracts. It receives external requests, translates them into commands for the business layer, and returns formatted responses.

#### Business Logic Layer
- The core of the application. It enforces business rules, processes data, and coordinates tasks. It is independent of any specific user interface or database technology.

#### Persistence Layer
- Handles all data storage and retrieval. It translates application objects into database records and vice versa, insulating the business logic from database-specific details.

---

## Business Logic Diagram

![Business Logic Class Diagram](./images/business_logic_class_diagram.jpg)

### Class Responsibilities

**Base Class**  
- Attributes: uuid, created_at, updated_at  
- Methods: Inherited by all classes

**User**  
- Attributes: first_name, last_name, email, password, is_host  
- Methods: register, update, delete, list, list_all_places

**Review**  
- Attributes: owner_id, place_id, rating, comment  
- Methods: create, update, delete, list_review(s)

**Place**  
- Attributes: owner_id, title, description, price, latitude, longitude, list_of_amenities  
- Methods: create, update, delete, list_place(s), list_all_places

**Amenities**  
- Attributes: name, description  
- Methods: create, delete, list_amenity, list_all_amenities

---

## API Sequence Diagrams

### User Registration Flow
![User Registration Flow](./images/user_creation_flow.png)

#### User Registration Summary
1. **Client → API Service**  
   `POST /users/register {username, email, password}`  

2. **Validation (API Service)**  
   - Invalid/missing fields → **400 Bad Request**  
   - Valid → continue  

3. **Check User (Business Logic → DB)**  
   - Exists → **409 Conflict (User/email exists)**  
   - Not exists → continue  

4. **Create User (Business Logic)**  
   - Hash password  
   - Create user instance  
   - Save to DB  

5. **Save Result (DB)**  
   - Error → **500 Internal Server Error**  
   - Success → **201 Created + user details**  

#### User Registration Code Legend
- **400** → Bad input  
- **409** → Duplicate user  
- **500** → DB error  
- **201** → User created  
- Password is always **hashed** before saving  

### Place Creation Flow
![Place Creation Flow](./images/place_creation_flow.png)

#### Place Creation Summary
1. **Client Request**  
   `POST /places` with authentication token and place data  

2. **Authentication**  
   - Token verified by **Auth Service**  
   - Invalid/expired → **401 Unauthorized**  

3. **Validation**  
   - Place data checked  
   - Invalid → **400 Bad Request**  

4. **Authorization**  
   - User permissions verified  
   - Unauthorized → **403 Forbidden**  

5. **Place Creation**  
   - Instance created and persisted  
   - DB error → **500 Internal Server Error**  

6. **Response**  
   - Success → **201 Created** with place details  

#### Place Creation Code Legend
- **400** → Bad input  
- **401** → Unauthorized  
- **403** → Forbidden  
- **500** → DB error  
- **201** → Place created  

### Review Submission Flow
![Review Submission Flow](./images/review%20flow.png)

#### Review Submission Summary
1. **Validation**  
   - Check if **User** and **Place** exist  
   - If missing → **404 Not Found**  

2. **Input Checking**  
   - Validate `rating` and `comment` fields  
   - Invalid → **400 Bad Request**  

3. **Review Creation**  
   - New review instance created  

4. **Persistence Layer**  
   - Saves to database  
   - Error → **500 Internal Server Error**  

5. **Response**  
   - Success → **201 Created** with review details  

#### Review Submission Code Legend
- **400** → Bad input  
- **404** → User or Place not found  
- **500** → DB error  
- **201** → Review created  

### Fetching Places Flow
![Fetching Places Flow](./images/fetching_places_flow.png)

#### Fetching Places Summary
1. **Input Validation**  
   - Filters checked before querying DB  

2. **Error Handling**  
   - Invalid → **400 Bad Request**  
   - No data → **200 OK** with empty list  
   - DB error → **500 Internal Server Error**  
   - Success → **200 OK** with results  

3. **Layered Responsibility**  
   - **Presentation Layer:** Validation, formatting, error messages  
   - **Business Logic Layer:** Processing and orchestration  
   - **Persistence Layer:** Raw data retrieval/storage  

#### Fetching Places Code Legend
- **400** → Bad input  
- **500** → DB error  
- **200** → OK (with results or empty list)  

---

## License

This project is for educational purposes only and is part of the **Holberton School** / **Foundations of Computer Science** curriculum.

---

## Authors

<p>
  <strong>Alba Eftimi</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <strong>Sokol Gjeka</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <strong>Renis Vukaj</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <strong>Kevin Voka</strong>

  GitHub: <a href="https://github.com/abfabs">abfabs</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  GitHub: <a href="https://github.com/sokolgj19">sokolgj19</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  GitHub: <a href="https://github.com/renisv">renisv</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  GitHub: <a href="https://github.com/kevin10v">kevin10v</a>
</p>

<p align="center">
  <em>September 2025</em><br>
  <em>Tirana, Albania</em>
</p>
