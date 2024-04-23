from models.product import Product
from database import db 

# for app context 
from main import app
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



for product in products : 
    new_product =  Product(id = int(product.get('id')), name=product.get('name'), quantity=product.get('quantity'), price=product.get('price'))
    db.session.add(new_product)
    db.session.commit()