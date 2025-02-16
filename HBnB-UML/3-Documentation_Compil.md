# HBnB Technical Documentation

## Introduction

This document serves as a comprehensive technical guide for the HBnB project, detailing the architecture, design, and interactions between various components. It consolidates the high-level package diagram, detailed class diagram for the Business Logic Layer, and sequence diagrams for API calls. This document aims to provide a clear reference for implementation phases and system architecture, ensuring consistency and clarity throughout the project.

### High-Level Package Diagram

```mermaid
classDiagram
class PresentationLayer {
    <<Interface>>
    +ServiceAPI
    +Services
    + API endpoints
}
class BusinessLogicLayer {
    +ModelClasses
    +User
    +Place
    +Review
    +Amenity

}
class PersistenceLayer {
    +DatabaseAccess
}
PresentationLayer --> BusinessLogicLayer : Facade Pattern
BusinessLogicLayer --> PersistenceLayer : Database Operations
```

## Explanation

- Presentation Layer: Handles user interactions and exposes APIs to clients.
- Business Logic Layer: Encapsulates the core logic and models, including User, Place, Review, and Amenity.
- Persistence Layer: Manages data storage and retrieval via database operations.
- Facade Pattern: Facilitates communication between layers, providing a unified interface and simplifying interactions.

### ClassDiagram

```mermaid
classDiagram
class User {
    #user_id: String
    +first_name: String
    +last_name: String
    +email: String
    -password: String
    -is_admin: boolean
    +register_user(): void
    +update_user(): void
    +delete_user(): void
    +authenticate_user(): boolean
}
class Place {
    #place_id: String
    +title: String
    +description: String
    +price_per_night: float
    +latitude: float
    +longitude: float
    #owner_id: String
    +create_place(): void
    +update_place(): void
    +delete_place(): void
    +list_place(): void
    +add_amenity(amenity: Amenity): void
}
class Review {
    #review_id: String
    +rating: int
    +comment: String
    +review_date: Date
    +create_review(): void
    +delete_review(): void
    +list_reviews(): List<Review>
}
class Amenity {
    #amenity_id: String
    +name: String
    +description: String
    +create_amenity(): void
    +delete_amenity(): void
    +list_amenities(): List<Amenity>
}
User --> Place : owns
User --> Place : searches
User --> Review : makes
Place --> Review : has
Place --> Amenity : contains
```

# Explanation

- User: Represents system users with methods to register, authenticate, and manage accounts.
- Place: Represents places listed by users, allowing creation, update, deletion, and listing of places.
- Review: Captures user feedback for places, including ratings and comments.
- Amenity: Represents additional features linked to places, such as pools or parking.

Relationships:
-User owns Place and submits Review.
-Place is associated with Review and contains Amenity.

### API Interaction Flow
## HbnB - sequenceDiagram

1. User Registration
```mermaid
sequenceDiagram
    participant User
    participant APIGateway
    participant UserService
    participant PersistenceLayer
    User->>APIGateway: Send registration request
    APIGateway->>UserService: Forward request
    UserService->>UserService: Validate input data
    UserService-->>PersistenceLayer: Store user data
    PersistenceLayer-->>UserService: Confirm storage
    UserService-->>APIGateway: Send confirmation response
    APIGateway-->>User: Return response
```

2. Place Creation
```mermaid
    participant User
    participant APIGateway
    participant PlaceService
    participant PersistenceLayer
    User->>APIGateway: Submit place details
    APIGateway->>PlaceService: Forward request
    PlaceService->>PlaceService: Validate request
    PlaceService-->>PersistenceLayer: Store place data
    PersistenceLayer-->>PlaceService: Confirm storage
    PlaceService-->>APIGateway: Send confirmation
    APIGateway-->>User: Return place ID
```

3. Review Submission
```mermaid
    participant User
    participant APIGateway
    participant ReviewService
    participant PersistenceLayer
    User->>APIGateway: Submit review
    APIGateway->>ReviewService: Forward request
    ReviewService->>ReviewService: Validate review
    ReviewService-->>PersistenceLayer: Store review data
    PersistenceLayer-->>ReviewService: Confirm storage
    ReviewService-->>APIGateway: Send success response
    APIGateway-->>User: Return confirmation
```

4. Fetching a List of Places
```mermaid
    participant User
    participant APIGateway
    participant PlaceService
    participant PersistenceLayer
    User->>APIGateway: Send search request
    APIGateway->>PlaceService: Forward request
    PlaceService->>PersistenceLayer: Query places
    PersistenceLayer-->>PlaceService: Return place data
    PlaceService->>PlaceService: Format response
    PlaceService-->>APIGateway: Send response
    APIGateway-->>User: Return list of places
```

# Explanation

- User Registration: Captures user details, validates them, and stores the information in the database.
- Place Creation: Allows users to create and save a new place listing with relevant details.
- Review Submission: Enables users to add reviews for a place, storing the data for future reference.
- Fetching Places: Queries the database for places based on user-provided criteria and formats the result.

## Conclusion

This document provides a detailed overview of the HBnB system architecture and design. It outlines the high-level package diagram, detailed class diagram for the Business Logic Layer, and sequence diagrams for critical API calls. This blueprint serves as a reference throughout the development phases, ensuring a consistent and efficient implementation process.
