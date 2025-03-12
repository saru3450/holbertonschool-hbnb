from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from app.services import facade
from app.routes.auth import login_required
from app.storage import storage
from app.routes.user import User

api = Namespace('users', description='User operations')

# Modèle Swagger pour les utilisateurs
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='Last name'),
    'email': fields.String(required=True, description='Email of the user')
})


@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    def post(self):
        """ Register a new user """
        user_data = api.payload

        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        new_user = facade.create_user(user_data)
        return {
            'id': new_user.id,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'email': new_user.email
        }, 201


@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """ Get user details by ID """
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return user.to_dict(), 200

    @api.expect(user_model, validate=True)
    @api.response(200, 'User successfully updated')
    @api.response(403, 'Forbidden: Cannot update another user')
    @api.response(404, 'User not found')
    @login_required  # 🔒 Protection de la modification de l'utilisateur
    def put(self, current_user_id, user_id):
        """ Update a user (only if it's the current user) """
        if user_id != current_user_id:
            return {'error': 'Forbidden: You can only update your own profile'}, 403

        user = storage.get(User, user_id)
        if not user:
            return {'error': 'User not found'}, 404

        data = request.get_json()

        # Empêcher la modification de l'email et du mot de passe
        if "email" in data or "password" in data:
            return {'error': 'Cannot modify email or password via this route'}, 403

        user.update(data)
        storage.save()
        return user.to_dict(), 200
