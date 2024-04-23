from crypt import methods
from flask import Flask
from database import configure_with_database, db
from controllers import authentication , product_controller

from models.user import User


app = Flask(__name__)
app = configure_with_database(app)


@app.route('/register', methods=['POST'])
def signup() : 
    return authentication.register_user()



@app.route('/login', methods=['POST'])
def login(): 
    return authentication.login()


@app.route('/order', methods=['POST'])
def order(): 
    return product_controller.order()

## for testing 
@app.route('/add' , methods=['GET'])
def add():
    # product =  Product(name='Book', quantity=50,  price=175.5)
    # db.session.add(product)
    # user = User(username='mohamed', email='mdiaa@gmail.com', address='october city')

    # db.session.add(user)

    user = db.session.query(User).filter(User.id == 1 ).first()
    # product = db.session.query(Product).filter(Product.id == 1 ).first()
    
    # user.products.append(product)
    # print('user: ', user, " product: ", product)

    # purchase = Purchase(user_id=user.id, product_id=product.id, cost = product.price * 1)


    # db.session.add(purchase)
    # db.session.commit()


    ## selecting data
    # print(user.products[0])
    # print(db.session.query(Purchase).filter(Purchase.user_id == user.id).first().cost)

    db.session.close()
    print('added')
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True, port=5000)



