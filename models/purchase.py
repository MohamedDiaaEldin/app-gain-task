
from sqlalchemy import ForeignKey
from database import db
from sqlalchemy.orm import relationship


## association table
class Purchase(db.Model):
    __tablename__ = 'purchases' 
    user_id = db.Column(db.Integer, ForeignKey('users.id'), primary_key=True) 
    product_id = db.Column(db.Integer, ForeignKey('products.id'), primary_key=True) 
    cost = db.Column(db.Double, nullable=False)

    # defines the relationships 
    # user = relationship('User', back_populates='Product')
    # product = relationship('Product', back_populates='User')

    def __repr__(self):
        return f'<User ID:{self.user_id}, Product ID: {self.product_id}>'
