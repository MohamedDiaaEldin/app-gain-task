from models.product import Product
from models.user_account import UserAcount
from database import db 

# for app context 
from main import app


# Products App Data
products = [
    {
        'id' : '5645'  , 
        'name' : 'Mac Pro', 
        'quantity':50, 
        'price':80000
    }, 
    {   'id':'5648' , 
        'name' : 'Dell inspiron 15', 
        'quantity':100, 
        'price':20000
    }, 
    {   'id':'5498' , 
        'name' : 'iphone X', 
        'quantity': 70, 
        'price':50000
    }
]



# Payment Gateway Data
users = [
    {
        'username':'mohamed', 
        'card_number':123564565456465 , 
        'exp_date':'12/29', 
        'csv' : 548 , 
        'balance': 5000 
    },
    {
        'username':'ali', 
        'card_number':654564651235645 , 
        'exp_date':'11/25', 
        'csv' : 654 , 
        'balance': 10000000
    }
]

def add_products():
    for product in products : 
        new_product =  Product(id = int(product.get('id')), name=product.get('name'), quantity=product.get('quantity'), price=product.get('price'))
        db.session.add(new_product)
        db.session.commit()

def add_user_accounts(): 
    for user in users : 
        new_user =  UserAcount(card_number = user.get('card_number')  ,  username=user.get('username'), exp_date=user.get('exp_date'), csv=user.get('csv'), balance=user.get('balance'))
        db.session.add(new_user)
        db.session.commit()



add_products()
add_user_accounts() 