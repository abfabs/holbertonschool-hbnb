from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from app.services import facade

api = Namespace('auth', description='Authentication operations')

# Model for input validation
login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    @api.response(200, 'Logged in successfully')
    @api.response(401, 'Invalid credentials')
    def post(self):
        """Authenticate user and return a JWT token"""
        credentials = api.payload  # Get the email and password from the request payload
        
        # Step 1: Retrieve the user based on the provided email
        user = facade.get_user_by_email(credentials['email'])
        
        # Step 2: Check if the user exists and the password is correct
        if not user or not user.verify_password(credentials['password']):
            return {'error': 'Invalid credentials'}, 401

        # Step 3: Create a JWT token with the user's id and is_admin flag
        access_token = create_access_token(
            identity=str(user.id),   # only user ID goes here
            additional_claims={"is_admin": user.is_admin}  # extra info here
        )
        
        # Step 4: Return the JWT token to the client
        return {'access_token': access_token}, 200

@api.route('/protected')
class ProtectedResource(Resource):
    @jwt_required()
    @api.response(200, 'Logged in successfully')
    @api.response(401, 'Invalid token')
    def get(self):
        """A protected endpoint that requires a valid JWT token"""

        current_user_id = get_jwt_identity() # Retrieve the user's identity from the token
        #if you need to see if the user is an admin or not, you can access additional claims using get_jwt() :
        claims = get_jwt()
        #additional claims["is_admin"] -> True or False
        return {
                'message': f'Hello, user {current_user_id}', 
                'user_id': current_user_id,
                'is_admin': claims.get('is_admin')
        }, 200