from app.models.user import User

def test_user_creation():
    user = User(first_name="Alice", last_name="Smith", email="alice@example.com")
    
    assert isinstance(user.id, str)  # Vérifie que l'ID est une chaîne UUID
    assert user.first_name == "Alice"
    assert user.last_name == "Smith"
    assert user.email == "alice@example.com"
    assert user.is_admin is False  # Par défaut, un utilisateur n'est pas admin
    print("✅ Test création utilisateur : OK")

test_user_creation()
