
from database import db
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'users' 
    id = db.Column(db.Integer, primary_key=True) ## auto increment 
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(120),  nullable=False)

    # defines the relationships
    products = relationship('Product', secondary='purchases', back_populates='users')

    def __repr__(self):
        return f'<User {self.username}>'
