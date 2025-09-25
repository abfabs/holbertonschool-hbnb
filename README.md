![Logo](./images/hbnb.jpg)

# HBnB Evolution - Airbnb Clone Project

---

## Objective
HBnB Evolution is an educational project that implements a simplified Airbnb-like platform to demonstrate:
- Modern web application architecture patterns
- Layered architecture implementation  
- Business logic modeling best practices
- API design and development
- Database-agnostic persistence layer design

---

## Key Functionalities
- **User Management**: Registration, profile updates, role-based access (users vs administrators)
- **Property Listings**: Create, update, manage listings with descriptions, pricing, and geolocation
- **Review System**: Rating and comment system for visited properties
- **Amenity Management**: Catalog system for property amenities with many-to-many relationships
- **Audit Trail**: Automatic creation/update timestamp tracking for all entities

---

## Design Architecture

### Package Diagram
![Package Diagram](./images/package_diagram.jpg)

---

## Architecture Overview

### Three-Layer Architecture

**Presentation Layer**
- Provides the user interface and API contracts. It receives external requests, translates them into commands for the business layer, and returns formatted responses.

**Business Logic Layer**
- The core of the application. It enforces business rules, processes data, and coordinates tasks. It is independent of any specific user interface or database technology.

**Persistence Layer**
- Handles all data storage and retrieval. It translates application objects into database records and vice versa, insulating the business logic from database-specific details.

---

## Project Status
**Phase 1**: Technical Documentation (Current)
- High-Level Package Diagram ✅
- Detailed Class Diagram for Business Logic Layer 
- Sequence Diagrams for API Calls
- Documentation Compilation

---

## License

This project is for educational purposes only and is part of the **Holberton School** / *Foundations of Computer Science* curriculum.

---

## Authors

<p>
  <strong>Alba Eftimi</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <strong>Sokol Gjeka</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <strong>Renis Vukaj</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <strong>Kevin Voka</strong>
</p>
<p>
  GitHub: <a href="https://github.com/abfabs">abfabs</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  GitHub: <a href="https://github.com/sokolgj19">sokolgj19</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  GitHub: <a href="https://github.com/renisv">renisv</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  GitHub: <a href="https://github.com/kevin10v">kevin10v</a>
</p>

---

<p align="center">
  <em>September 2025</em><br>
  <em>Tirana, Albania</em>
</p>
