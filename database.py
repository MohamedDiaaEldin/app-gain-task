
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from read_env import get_env

DATABASE_URL = get_env('DATABASE_URL')


db = SQLAlchemy()

def configure_with_database(app):
    print('database url ---> ', DATABASE_URL)
    # app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False    
    
    app.app_context().push()    
        
    with app.app_context():
        db.init_app(app)   
    
    # configure migration
    Migrate(app, db)
    from models.user import User
    
    return app


