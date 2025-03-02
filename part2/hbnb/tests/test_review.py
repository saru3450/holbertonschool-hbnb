from app.models.review import Review
from app.models.user import User
from app.models.place import Place

def test_review_creation():
    user = User(first_name="Emma", last_name="Watson", email="emma@example.com")
    place = Place(title="Chalet à la montagne", description="Vue imprenable", price=200, latitude=48.5, longitude=6.3, owner=user)
    review = Review(text="Incroyable séjour !", rating=5, place=place, user=user)

    assert isinstance(review.id, str)
    assert review.text == "Incroyable séjour !"
    assert 1 <= review.rating <= 5  # Vérifie que la note est correcte
    assert review.place == place
    assert review.user == user
    print("✅ Test création d'un avis : OK")

test_review_creation()
