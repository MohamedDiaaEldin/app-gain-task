from flask import Flask

from database import configure_with_database, db
from controllers.authentication import add_user
from models.product import Product
from models.user import User
from models.purchase import Purchase

app = Flask(__name__)
app = configure_with_database(app)

@app.route('/' , methods=['POST'])
def index():
    return add_user()



## for testing 
@app.route('/add' , methods=['GET'])
def add():
    # product =  Product(name='Book', quantity=50,  price=175.5)
    # db.session.add(product)
    # user = User(username='mohamed', email='mdiaa@gmail.com', address='october city')

    # db.session.add(user)

    db.session    
    db.session.commit()

    db.session.close()
    print('added')
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True, port=5000)



