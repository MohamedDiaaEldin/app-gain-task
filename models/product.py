
from database import db
from sqlalchemy.orm import relationship

class Product(db.Model):
    __tablename__ = 'products' 
    id = db.Column(db.Integer, primary_key=True) ## auto increment 
    name = db.Column(db.String(80), unique=True, nullable=False)    
    quantity = db.Column(db.Integer)
    price = db.Column(db.Double) 
    # defines the relationships 
    
    users = relationship('User', secondary='purchases', back_populates='products')
    @staticmethod
    def get_product_by_id(id): 
        return db.session.query(Product).filter(Product.id == id).first()

    def __repr__(self):
        return f'<Product Name: {self.name}>'
