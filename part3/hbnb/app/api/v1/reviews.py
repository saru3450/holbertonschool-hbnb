from flask_restx import Namespace, Resource, fields
from flask import request
from app.services.facade import HBnBFacade

api = Namespace('reviews', description='Operations sur les avis')
facade = HBnBFacade()

review_model = api.model('Review', {
    'text': fields.String(required=True, description='Texte du commentaire'),
    'rating': fields.Integer(required=True, description='Note (1-5)'),
    'user_id': fields.String(required=True, description='ID de l’utilisateur'),
    'place_id': fields.String(required=True, description='ID du lieu')
})


@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Avis créé avec succès')
    def post(self):
        """ Créer un nouvel avis """
        data = request.json
        review = facade.create_review(data)
        return vars(review), 201

    @api.response(200, 'Liste des avis récupérée')
    def get(self):
        """ Récupérer tous les avis """
        reviews = facade.get_all_reviews()
        return [vars(r) for r in reviews], 200


@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Avis récupéré avec succès')
    def get(self, review_id):
        """ Récupérer un avis par ID """
        review = facade.get_review(review_id)
        if not review:
            return {'message': 'Avis non trouvé'}, 404
        return vars(review), 200

    @api.expect(review_model)
    @api.response(200, 'Avis mis à jour')
    def put(self, review_id):
        """ Mettre à jour un avis """
        data = request.json
        review = facade.update_review(review_id, data)
        if not review:
            return {'message': 'Avis non trouvé'}, 404
        return {'message': 'Avis mis à jour'}, 200

    @api.response(200, 'Avis supprimé')
    def delete(self, review_id):
        """ Supprimer un avis """
        success = facade.delete_review(review_id)
        if not success:
            return {'message': 'Avis non trouvé'}, 404
        return {'message': 'Avis supprimé'}, 200


@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'Liste des avis pour un lieu')
    def get(self, place_id):
        """ Récupérer tous les avis d'un lieu """
        reviews = facade.get_reviews_by_place(place_id)
        return [vars(r) for r in reviews], 200
