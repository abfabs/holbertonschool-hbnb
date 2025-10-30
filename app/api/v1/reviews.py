from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade

api = Namespace('reviews', description='Review operations')

review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewListResource(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(401, 'Unauthorized')
    @jwt_required()
    def post(self):
        current_user_id = get_jwt_identity()
        review_data = api.payload
        review_data['user_id'] = current_user_id

        try:
            new_review = facade.create_review(review_data)
            return {
                'id': new_review.id,
                'text': new_review.text,
                'rating': new_review.rating,
                'user_id': new_review.user.id,
                'place_id': new_review.place.id
            }, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        all_reviews = facade.get_all_reviews()
        return [{
            'id': review.id,
            'text': review.text,
            'rating': review.rating,
            'user_id': review.user.id,
            'place_id': review.place.id
        } for review in all_reviews], 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        
        return {
            'id': review.id,
            'text': review.text,
            'rating': review.rating,
            'user_id': review.user.id,
            'place_id': review.place.id
        }, 200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(403, 'Unauthorized action')
    @api.response(400, 'Invalid input data')
    @api.response(401, 'Unauthorized')
    @jwt_required()
    def put(self, review_id):
        current_user_id = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get('is_admin', False)
        
        review_data = api.payload
        review = facade.get_review(review_id)
        
        if not review:
            return {'error': 'Review not found'}, 404
        
        if not is_admin and review.user.id != current_user_id:
            return {'error': 'Unauthorized action'}, 403
        
        try:
            updated_review = facade.update_review(review_id, review_data)
            return {
                'id': updated_review.id,
                'text': updated_review.text,
                'rating': updated_review.rating,
                'user_id': updated_review.user.id,
                'place_id': updated_review.place.id
            }, 200
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    @api.response(403, 'Unauthorized action')
    @api.response(500, 'Failed to delete review')
    @api.response(401, 'Unauthorized')
    @jwt_required()
    def delete(self, review_id):
        current_user_id = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get('is_admin', False)
        
        review = facade.get_review(review_id)
        
        if not review:
            return {'error': 'Review not found'}, 404
        
        if not is_admin and review.user.id != current_user_id:
            return {'error': 'Unauthorized action'}, 403
        
        success = facade.delete_review(review_id)
        if not success:
            return {'error': 'Failed to delete review'}, 500
        
        return {'message': 'Review deleted successfully'}, 200
