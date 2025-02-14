sequenceDiagram
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