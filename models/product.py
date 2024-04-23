"""
Product Model

This module defines the Product model for the application.

Model:
    - Product: Represents a product available in the system.

Attributes:
    - id: Unique identifier for the product.
    - name: Name of the product.
    - quantity: Quantity of the product available.
    - price: Price of the product.

Methods:
    - get_product_by_id: Retrieves a product by its ID.

"""

from database import db
from sqlalchemy.orm import relationship

class Product(db.Model):
    """
    Represents a product available in the system.

    Attributes:
        id (int): Unique identifier for the product.
        name (str): Name of the product.
        quantity (int): Quantity of the product available.
        price (float): Price of the product.
    """
    __tablename__ = 'products' 
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(80), unique=True, nullable=False)    
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float) 

    # Defines the relationships 
    users = relationship('User', secondary='purchases', back_populates='products')

    @staticmethod
    def get_product_by_id(id): 
        """
        Retrieves a product by its ID.

        Args:
            id (int): The ID of the product to retrieve.

        Returns:
            Product: The product object if found, None otherwise.
        """
        return db.session.query(Product).filter(Product.id == id).first()

    def __repr__(self):
        """
        String representation of the Product object.

        Returns:
            str: The string representation of the Product object.
        """
        return f'<Product Name: {self.name}>'
