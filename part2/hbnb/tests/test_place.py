from app.models.place import Place
from app.models.user import User

def test_place_creation():
    owner = User(first_name="John", last_name="Doe", email="john@example.com")
    place = Place(title="Maison en bord de mer", description="Superbe vue", price=150, latitude=45.0, longitude=-1.2, owner=owner)

    assert isinstance(place.id, str)
    assert place.title == "Maison en bord de mer"
    assert place.description == "Superbe vue"
    assert place.price == 150.0  # Doit être un float positif
    assert -90.0 <= place.latitude <= 90.0  # Latitude valide
    assert -180.0 <= place.longitude <= 180.0  # Longitude valide
    assert place.owner == owner  # Vérifie que l'objet `User` est bien le propriétaire
    print("✅ Test création d'un lieu : OK")

test_place_creation()
