from flask import Blueprint, jsonify, request
from app.routes.amenity import Amenity

amenity_bp = Blueprint('amenity', __name__)

@amenity_bp.route('/', methods=['GET'])
def get_amenities():
    amenities = []  # Logique pour récupérer les commodités
    return jsonify(amenities)

@amenity_bp.route('/', methods=['POST'])
def create_amenity():
    data = request.get_json()
    amenity = Amenity(name=data["name"], description=data["description"])
    # Logique pour ajouter la commodité à la base de données
    return jsonify({"message": "Amenity created", "amenity": amenity.to_dict()}), 201
