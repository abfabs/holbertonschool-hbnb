from app import create_app
from app.services import facade
from app.extensions import db

app = create_app(config_class='config.DevelopmentConfig')

with app.app_context():
    db.create_all()
    print("Database tables created!")
    
    try:
        admin_data = {
            "first_name": "Admin",
            "last_name": "User",
            "email": "admin@hbnb.com",
            "password": "admin123",
            "is_admin": True
        }
        admin_user = facade.create_user(admin_data)
        print(f"Admin user created: {admin_user.email}")
    except ValueError:
        print("Admin user already exists")

if __name__ == '__main__':
    app.run(debug=True)
