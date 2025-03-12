from app.storage import storage
from app.models.user import User

# Ajouter un utilisateur
new_user = User(first_name="John", last_name="Doe", email="john@example.com", password="1234")
storage.new(new_user)
storage.save()

# Récupérer un utilisateur
user = storage.get(User, new_user.id)
print(user.to_dict())

# Supprimer un utilisateur
storage.delete(user)
