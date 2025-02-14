### HbnB - sequenceDiagram
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
