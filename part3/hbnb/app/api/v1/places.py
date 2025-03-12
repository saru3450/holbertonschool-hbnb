from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from app.models.place import Place
from app.storage import storage
from app.routes.auth import login_required
from app.services import facade

api = Namespace('places', description='Place operations')

# Modèles Swagger pour la documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude'),
    'longitude': fields.Float(required=True, description='Longitude'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="Amenity IDs")
})


@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    @login_required  # 🔒 Protège la création d’un lieu
    def post(self, user_id):
        """Créer un nouveau lieu (réservé aux utilisateurs connectés)"""
        data = request.get_json()
        data["owner_id"] = user_id  # Assure que l'owner_id est bien celui de l'utilisateur connecté
        new_place = facade.create_place(data)
        return new_place.to_dict(), 201

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Récupérer la liste de tous les lieux"""
        places = facade.get_all_places()
        return [place.to_dict() for place in places], 200


@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Obtenir les détails d’un lieu par son ID"""
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404
        return place.to_dict(), 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(403, 'Forbidden: You are not the owner')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    @login_required  # 🔒 Protège la modification d’un lieu
    def put(self, user_id, place_id):
        """Mettre à jour un lieu (seulement par le propriétaire)"""
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404

        if place.owner_id != user_id:
            return {"error": "Forbidden: You are not the owner"}, 403

        data = api.payload
        updated_place = facade.update_place(place_id, data)
        return updated_place.to_dict(), 200

    @api.response(200, 'Place deleted successfully')
    @api.response(403, 'Forbidden: You are not the owner')
    @api.response(404, 'Place not found')
    @login_required  # 🔒 Protège la suppression d’un lieu
    def delete(self, user_id, place_id):
        """Supprimer un lieu (seulement par le propriétaire)"""
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404

        if place.owner_id != user_id:
            return {"error": "Forbidden: You are not the owner"}, 403

        facade.delete_place(place_id)
        return {"message": "Place deleted successfully"}, 200
