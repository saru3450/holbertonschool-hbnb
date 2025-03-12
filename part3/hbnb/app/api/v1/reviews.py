from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from app.services.facade import HBnBFacade
from app.models.review import Review
from app.models.place import Place
from app.routes.auth import login_required
from app.storage import storage

api = Namespace('reviews', description='Operations sur les avis')
facade = HBnBFacade()

# Modèle Swagger pour les avis
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Texte du commentaire'),
    'rating': fields.Integer(required=True, description='Note (1-5)'),
    'place_id': fields.String(required=True, description='ID du lieu')
})


@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'Liste des avis pour un lieu récupérée')
    def get(self, place_id):
        """ Récupérer tous les avis d'un lieu """
        reviews = facade.get_reviews_by_place(place_id)
        return [r.to_dict() for r in reviews], 200

    @api.expect(review_model)
    @api.response(201, 'Avis créé avec succès')
    @api.response(403, 'Interdit : vous ne pouvez pas noter votre propre lieu')
    @api.response(400, 'Données invalides')
    @login_required  # Protection de l'ajout d'avis
    def post(self, user_id, place_id):
        """ Créer un nouvel avis sur un lieu """
        place = storage.get(Place, place_id)
        if not place:
            return {"error": "Place not found"}, 404

        if place.owner_id == user_id:
            return {"error": "You cannot review your own place"}, 403

        existing_review = storage.find_one(Review, {"user_id": user_id, "place_id": place_id})
        if existing_review:
            return {"error": "You have already reviewed this place"}, 403

        data = request.get_json()
        new_review = facade.create_review(user_id=user_id, place_id=place_id, data=data)
        return new_review.to_dict(), 201


@api.route('/reviews/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Avis récupéré avec succès')
    @api.response(404, 'Avis non trouvé')
    def get(self, review_id):
        """ Récupérer un avis par son ID """
        review = facade.get_review(review_id)
        if not review:
            return {"message": "Avis non trouvé"}, 404
        return review.to_dict(), 200

    @api.expect(review_model)
    @api.response(200, 'Avis mis à jour avec succès')
    @api.response(403, 'Interdit : Vous ne pouvez modifier que vos propres avis')
    @api.response(404, 'Avis non trouvé')
    @login_required  #  Protection de la mise à jour d'un avis
    def put(self, user_id, review_id):
        """ Modifier un avis (seulement si l'utilisateur est l'auteur) """
        review = facade.get_review(review_id)
        if not review:
            return {"message": "Avis non trouvé"}, 404

        if review.user_id != user_id:
            return {"error": "You can only update your own review"}, 403

        data = request.get_json()
        updated_review = facade.update_review(review_id, data)
        return updated_review.to_dict(), 200

    @api.response(200, 'Avis supprimé avec succès')
    @api.response(403, 'Interdit : Vous ne pouvez supprimer que vos propres avis')
    @api.response(404, 'Avis non trouvé')
    @login_required  #  Protection de la suppression d'un avis
    def delete(self, user_id, review_id):
        """ Supprimer un avis (seulement si l'utilisateur est l'auteur) """
        review = facade.get_review(review_id)
        if not review:
            return {"message": "Avis non trouvé"}, 404

        if review.user_id != user_id:
            return {"error": "You can only delete your own review"}, 403

        facade.delete_review(review_id)
        return {"message": "Avis supprimé avec succès"}, 200
