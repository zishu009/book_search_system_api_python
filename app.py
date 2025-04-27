from flask import Flask
from models import db
from routes import app_routes

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
    
    db.init_app(app)
    
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()  
    
    app_routes(app)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)