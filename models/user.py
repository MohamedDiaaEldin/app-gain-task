"""
User Model

This module defines the User model for the application.

Model:
    - User: Represents a user in the system.

Attributes:
    - id: Unique identifier for the user.
    - username: Username of the user.
    - email: Email address of the user.
    - password: Password of the user.
    - address: Address of the user.

"""

from database import db
from sqlalchemy.orm import relationship

class User(db.Model):
    """
    Represents a user in the system.

    Attributes:
        id (int): Unique identifier for the user.
        username (str): Username of the user.
        email (str): Email address of the user.
        password (str): Password of the user.
        address (str): Address of the user.
    """
    __tablename__ = 'users' 
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    address = db.Column(db.String(120),  nullable=False)

    # Defines the relationships
    products = relationship('Product', secondary='purchases', back_populates='users')

    @staticmethod
    def get_user_by_email(email): 
        """
        Retrieves a user by their email address.

        Args:
            email (str): The email address of the user to retrieve.

        Returns:
            User: The user object if found, None otherwise.
        """
        return db.session.query(User).filter(User.email == email).first()

    def __repr__(self):
        """
        String representation of the User object.

        Returns:
            str: The string representation of the User object.
        """
        return f'<User: {self.username}>'
