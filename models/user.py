
from database import db
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'users' 
    id = db.Column(db.Integer, primary_key=True) ## auto increment 
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    address = db.Column(db.String(120),  nullable=False)

    # defines the relationships
    products = relationship('Product', secondary='purchases', back_populates='users')

    @staticmethod
    def get_user_by_email(email): 
        return db.session.query(User).filter(User.email == email).first()
    def __repr__(self):
        return f'<User: {self.username}>'
