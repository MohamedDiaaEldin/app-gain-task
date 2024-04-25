"""
Database Configuration

This module configures the Flask application with SQLAlchemy for database management.

Functions:
    - configure_with_database: Configures the Flask application with SQLAlchemy and database migration.

"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from utilities.read_env import get_env

# Retrieve the database URL from environment variables
DATABASE_URL = get_env('DATABASE_URL')

# Initialize SQLAlchemy database object
db = SQLAlchemy()

def configure_with_database(app):
    """
    Configures the Flask application with SQLAlchemy and database migration.

    Args:
        app (Flask): The Flask application instance.

    Returns:
        Flask: The configured Flask application instance.
    """
    print('database url ---> ', DATABASE_URL)
    
    # Configure database connection settings
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Push the application context
    app.app_context().push()    

    # Initialize SQLAlchemy with the Flask application
    with app.app_context():
        db.init_app(app)   
    
    # Configure database migration
    Migrate(app, db)

    # Import models for migration
    from models.user import User 
    from models.product import Product 
    from models.purchase import Purchase
    from models.user_account import UserAcount

    return app
