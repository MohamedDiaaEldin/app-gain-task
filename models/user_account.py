
from database import db

class UserAcount(db.Model):
    __tablename__ = 'accounts' 
    card_number = db.Column(db.BigInteger, primary_key=True) 
    username = db.Column(db.String(50), nullable=False)
    exp_date = db.Column(db.String(5), unique=True, nullable=False)
    csv = db.Column(db.Integer, unique=True, nullable=False)
    balance = db.Column(db.Double)
    

    def __repr__(self):
        return f'<User: {self.username}, Card Number: {self.card_number}>'


    @staticmethod
    def process_payment(account_data) : 
        try: 
            account = db.session.query(UserAcount).filter(UserAcount.card_number == account_data.get('card_number')).first()                
            if  not account or account.exp_date != account_data.get('exp_date') or account.csv != account_data.get('csv')  or account.balance < account_data.get('amount') : 
                return 404  # User Not Fount or No Enough Balance 
            
            ## Subtract From User Balance
            account.balance = account.balance - account_data.get('amount') 

            
            db.session.add(account)
            db.session.commit()
            return 200 # Success
        except : 
            db.session.rollback()
            return 500 
        finally : 
            db.session.close()
        
    @staticmethod
    def add_balance(account_data): 
          
        try:                           
            account = db.session.query(UserAcount).filter(UserAcount.card_number == account_data.get('card_number')).first()                
            if  not account or account.exp_date != account_data.get('exp_date') or account.csv != account_data.get('csv')   : 
                return 404  # User Not Fount or No Enough Balance 
              
            ## Add To User Balance
            account.balance = account.balance + account_data.get('amount') 

            db.session.add(account)
            db.session.commit()
            return 200 # Success
        except : 
            db.session.rollback()            
            return 500
        finally : 
            db.session.close()
