from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import (
    jwt_required, get_jwt_identity
)
from app.services import facade

api = Namespace('admin', description='Admin operations')

user_model = api.model(
    'User', {
        'first_name': fields.String(
            required=True, description="User's first name"
        ),
        'last_name': fields.String(
            required=True, description="User's last name"
        ),
        'password': fields.String(
            required=True, description="User's password"
        ),
        'email': fields.String(
            required=True, description="User's email"
        ),
        'is_admin': fields.Boolean(
            required=True, description="Admin flag"
        )
    }
)

amenity_model = api.model(
    'Amenity', {
        'name': fields.String(
            required=True, description="Name of the amenity"
        )
    }
)

place_model = api.model(
    'Place', {
        'title': fields.String(
            required=True, description="Title of the place"
        ),
        'description': fields.String(
            description="Description of the place"
        ),
        'price': fields.Float(
            required=True, description="Price per night"
        ),
        'latitude': fields.Float(
            required=True, description="Latitude of the place"
        ),
        'longitude': fields.Float(
            required=True, description="Longitude of the place"
        ),
        'owner_id': fields.String(
            required=True, description="ID of the owner"
        )
    }
)


@api.route('/users/')
class AdminUserCreate(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, "User successfully created")
    @api.response(400, "Email already registered or invalid data")
    @api.response(403, "Admin privileges required")
    @api.doc(security='token')
    @jwt_required()
    def post(self):
        """Create a new user (Admin only)."""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': "Admin privileges required"}, 403

        user_data = api.payload
        email = user_data.get('email')

        if facade.get_user_by_email(email):
            return {'error': "Email already registered"}, 400

        try:
            new_user = facade.create_user(user_data)
            return {
                'id': new_user.id,
                'message': "User successfully created"
            }, 201
        except (ValueError, TypeError) as e:
            return {'error': str(e)}, 400


@api.route('/users/<user_id>')
class AdminUserModify(Resource):
    @api.expect(user_model, validate=True)
    @api.response(200, "User successfully updated")
    @api.response(400, "Invalid data or email already used")
    @api.response(403, "Admin privileges required")
    @api.response(404, "User not found")
    @api.doc(security='token')
    @jwt_required()
    def put(self, user_id):
        """Update an existing user (Admin only)."""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': "Admin privileges required"}, 403

        user_data = api.payload
        email = user_data.get('email')

        if email:
            existing_user = facade.get_user_by_email(email)
            if existing_user and str(existing_user.id) != user_id:
                return {'error': "Email already in use"}, 400

        try:
            updated_user = facade.update_user(user_id, user_data)
            return {
                'id': updated_user.id,
                'message': "User successfully updated"
            }, 200
        except facade.NotFoundError:
            return {'error': "User not found"}, 404
        except (ValueError, TypeError) as e:
            return {'error': str(e)}, 400


@api.route('/amenities/')
class AdminAmenityCreate(Resource):
    @api.expect(amenity_model)
    @api.response(201, "Amenity successfully created")
    @api.response(400, "Invalid data or amenity already registered")
    @api.response(403, "Admin privileges required")
    @api.doc(security='token')
    @jwt_required()
    def post(self):
        """Create a new amenity (Admin only)."""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': "Admin privileges required"}, 403

        amenity_data = api.payload

        if facade.get_amenity_by_name(amenity_data['name']):
            return {'error': "Amenity already registered"}, 400

        try:
            new_amenity = facade.create_amenity(amenity_data)
            return {
                'id': new_amenity.id,
                'message': "Amenity successfully created"
            }, 201
        except (ValueError, TypeError) as e:
            return {'error': str(e)}, 400


@api.route('/amenities/<amenity_id>')
class AdminAmenityModify(Resource):
    @api.expect(amenity_model)
    @api.response(200, "Amenity successfully updated")
    @api.response(400, "Invalid data")
    @api.response(403, "Admin privileges required")
    @api.response(404, "Amenity not found")
    @api.doc(security='token')
    @jwt_required()
    def put(self, amenity_id):
        """Update an existing amenity (Admin only)."""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': "Admin privileges required"}, 403

        amenity_data = api.payload

        try:
            updated_amenity = facade.update_amenity(amenity_id, amenity_data)
            return {
                'id': updated_amenity.id,
                'message': "Amenity successfully updated"
            }, 200
        except facade.NotFoundError:
            return {'error': "Amenity not found"}, 404
        except (ValueError, TypeError) as e:
            return {'error': str(e)}, 400

