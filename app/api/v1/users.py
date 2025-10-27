from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade
from app.services import facade



api = Namespace('users', description='User operations')


# Define the user model for input validation and documentation
user_input_model = api.model('UserInput', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password' : fields.String(required=True, description='Password of the user')
})


user_output_model = api.model('UserOutput', {
    'id': fields.String(required=True, description='id of the user'),
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'is_admin': fields.Boolean(required=True, description='Status of the user')
})

user_update_model = api.model('UserUpdate', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user')
})

@api.route('/')
class UserList(Resource):
    # Register a new user and return their details
    @api.expect(user_input_model, validate=True)
    @api.response(201, 'User successfully created', user_output_model)
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload


        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400


        try:
            new_user = facade.create_user(user_data)
            return {
                'id': new_user.id, 
                'first_name': new_user.first_name, 
                'last_name': new_user.last_name, 
                'email': new_user.email,
                'is_admin': new_user.is_admin
            }, 201
        except ValueError as e:
            return {'error': str(e)}, 400
        
    # Retrieve and return a list of all registered users
    @api.response(200, "all users are retrieved", [user_output_model])
    def get(self):
        all_users = facade.get_all_users()
        return [
            {
                'id': user.id, 
                'first_name': user.first_name, 
                'last_name': user.last_name, 
                'email': user.email,
                'is_admin': user.is_admin
            }
            for user in all_users
        ], 200
    
@api.route('/<user_id>')
@api.param('user_id', "unique user id")
class UserResource(Resource):
    # Retrieve and return details for a specific user by ID
    @api.response(200, 'User details retrieved successfully', user_output_model)
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {
            'id': user.id, 
            'first_name': user.first_name, 
            'last_name': user.last_name, 
            'email': user.email,
            'is_admin': user.is_admin
        }, 200
    


    # Update user information and return the updated details
    @api.expect(user_update_model, validate=True)
    @api.response(200, 'User successfully updated')
    @api.response(404, 'User not found')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def put(self, user_id):
        user_data = api.payload
        try:
            updated_user = facade.update_user(user_id, user_data)
            if not updated_user:
                return {'error': "User not found"}, 404
            return {
                'id': updated_user.id, 
                'first_name': updated_user.first_name, 
                'last_name': updated_user.last_name, 
                'email': updated_user.email,
                'is_admin': updated_user.is_admin
            }, 200
        except ValueError as e:
            return {'error': str(e)}, 400
