
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from utilities.read_env import get_env

DATABASE_URL = get_env('DATABASE_URL')


db = SQLAlchemy()

def configure_with_database(app):
    print('database url ---> ', DATABASE_URL)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False    
        # 

    app.app_context().push()    

    with app.app_context():
        db.init_app(app)   
    
    # Configure migration 
    Migrate(app, db)
    from models.user import User 
    from models.product import Product 
    from models.purchase import Purchase

    return app


