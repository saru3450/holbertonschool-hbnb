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
