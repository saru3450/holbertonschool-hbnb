```mermaid
erDiagram
    users {
        CHAR(36) id PK "Primary Key (UUID)"
        VARCHAR(255) first_name
        VARCHAR(255) last_name
        VARCHAR(255) email "Unique"
        VARCHAR(255) password "Hashed password"
        BOOLEAN is_admin "Default: FALSE"
    }

    places {
        CHAR(36) id PK "Primary Key (UUID)"
        VARCHAR(255) title
        TEXT description
        DECIMAL(10,2) price
        FLOAT latitude
        FLOAT longitude
        CHAR(36) owner_id FK "Foreign Key to users(id)"
    }

    reviews {
        CHAR(36) id PK "Primary Key (UUID)"
        TEXT text
        INT rating "Between 1 and 5"
        CHAR(36) user_id FK "Foreign Key to users(id)"
        CHAR(36) place_id FK "Foreign Key to places(id)"
    }

    amenities {
        CHAR(36) id PK "Primary Key (UUID)"
        VARCHAR(255) name "Unique"
    }

    place_amenities {
        CHAR(36) place_id FK "Foreign Key to places(id)"
        CHAR(36) amenity_id FK "Foreign Key to amenities(id)"
    }

    %% Relationships
    users ||--o{ places : "owns"
    places ||--o{ reviews : "has"
    places }o--o{ amenities : "includes"
```
