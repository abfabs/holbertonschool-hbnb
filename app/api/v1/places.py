from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade

api = Namespace('places', description='Place operations')

place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place')
})

def serialize_place(place):
    """Helper function to serialize place with amenities"""
    return {
        'id': place.id,
        'title': place.title,
        'description': place.description,
        'price': place.price,
        'latitude': place.latitude,
        'longitude': place.longitude,
        'owner_id': place.owner.id,
        'amenities': [{'id': amenity.id, 'name': amenity.name} for amenity in place.amenities]
    }

@api.route('/')
class PlaceListResource(Resource):
    @api.expect(place_model, validate=True)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(401, 'Invalid authorization data')
    @jwt_required()
    def post(self):
        current_user_id = get_jwt_identity()
        place_data = api.payload
        place_data['owner_id'] = current_user_id

        try:
            new_place = facade.create_place(place_data)
            return {
                'id': new_place.id,
                'title': new_place.title,
                'description': new_place.description,
                'price': new_place.price,
                'latitude': new_place.latitude,
                'longitude': new_place.longitude,
                'owner_id': new_place.owner.id,
                "amenities": [{"id": amenity.id, "name": amenity.name} for amenity in new_place.amenities]
            }, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        all_places = facade.get_all_places()
        return [{
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner_id': place.owner.id,
            "amenities": [{"id": amenity.id, "name": amenity.name} for amenity in place.amenities]
        } for place in all_places], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        
        # Get reviews for this place
        reviews = facade.get_reviews_by_place(place_id) or []
        
        return {
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner_id': place.owner.id,
            'owner': {
                'id': place.owner.id,
                'first_name': place.owner.first_name,
                'last_name': place.owner.last_name
            },
            'amenities': [{'id': amenity.id, 'name': amenity.name} for amenity in place.amenities],
            'reviews': [{
                'id': review.id,
                'text': review.text,
                'rating': review.rating,
                'created_at': review.created_at.isoformat(),
                'user': {
                    'id': review.user.id,
                    'first_name': review.user.first_name,
                    'last_name': review.user.last_name
                }
            } for review in reviews]
        }, 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(403, 'Unauthorized action')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, place_id):
        current_user_id = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get('is_admin', False)
        
        place_data = api.payload
        place = facade.get_place(place_id)
        
        if not place:
            return {'error': 'Place not found'}, 404
        
        if not is_admin and place.owner.id != current_user_id:
            return {'error': 'Unauthorized action'}, 403
        
        if 'owner_id' in place_data:
            del place_data['owner_id']
        
        try:
            updated_place = facade.update_place(place_id, place_data)
            return {
                'id': updated_place.id,
                'title': updated_place.title,
                'description': updated_place.description,
                'price': updated_place.price,
                'latitude': updated_place.latitude,
                'longitude': updated_place.longitude,
                'owner_id': updated_place.owner.id,
                "amenities": [{"id": amenity.id, "name": amenity.name} for amenity in updated_place.amenities]
            }, 200
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.response(200, 'Place deleted successfully')
    @api.response(404, 'Place not found')
    @api.response(403, 'Unauthorized action')
    @jwt_required()
    def delete(self, place_id):
        current_user_id = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get('is_admin', False)
        
        place = facade.get_place(place_id)
        
        if not place:
            return {'error': 'Place not found'}, 404
        
        if not is_admin and place.owner.id != current_user_id:
            return {'error': 'Unauthorized action'}, 403
        
        success = facade.delete_place(place_id)
        if not success:
            return {'error': 'Failed to delete place'}, 500
        
        return {'message': 'Place deleted successfully'}, 200

@api.route('/<place_id>/reviews')
class PlaceReviewListResource(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        reviews = facade.get_reviews_by_place(place_id)
        if reviews is None:
            return {'error': 'Place not found'}, 404
        
        return [{
            'id': review.id,
            'text': review.text,
            'rating': review.rating,
            'user_id': review.user.id
        } for review in reviews], 200

@api.route('/<place_id>/amenities')
class PlaceAmenityListResource(Resource):
    @api.response(200, 'Amenity successfully added to place')
    @api.response(404, 'Place or amenity not found')
    @api.response(403, 'Unauthorized action')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self, place_id):
        """Add an amenity to a place"""
        current_user_id = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get('is_admin', False)
        
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        
        if not is_admin and place.owner.id != current_user_id:
            return {'error': 'Unauthorized action'}, 403
        
        data = api.payload
        amenity_id = data.get('amenity_id')
        
        if not amenity_id:
            return {'error': 'Amenity ID is required'}, 400
        
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 404
        
        try:
            place.amenities.append(amenity)
            place.save()
            return serialize_place(place), 200
        except Exception as e:
            return {'error': str(e)}, 400
