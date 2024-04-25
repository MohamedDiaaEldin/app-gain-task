"""
Purchase Model

This module defines the Purchase model for the application.

Model:
    - Purchase: Represents a purchase made by a user.

Attributes:
    - id: Unique identifier for the purchase.
    - user_id: Foreign key referencing the user making the purchase.
    - product_id: Foreign key referencing the product being purchased.
    - cost: Cost of the purchase.

"""
from sqlalchemy import ForeignKey
from database import db

class Purchase(db.Model):
    """
    Represents a purchase made by a user.

    Attributes:
        id (int): Unique identifier for the purchase.
        user_id (int): Foreign key referencing the user making the purchase.
        product_id (int): Foreign key referencing the product being purchased.
        cost (float): Cost of the purchase.
    """
    __tablename__ = 'purchases'     
    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, ForeignKey('users.id')) 
    product_id = db.Column(db.Integer, ForeignKey('products.id')) 
    cost = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    paid = db.Column(db.Boolean, default=False)
    

    def __repr__(self):
        """
        String representation of the Purchase object.

        Returns:
            str: The string representation of the Purchase object.
        """
        return f'<User ID:{self.user_id}, Product ID: {self.product_id}>'
