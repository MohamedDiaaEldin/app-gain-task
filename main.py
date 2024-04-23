
from flask import Flask
from database import configure_with_database
from controllers import authentication , product_controller



app = Flask(__name__)
app = configure_with_database(app)


@app.route('/register', methods=['POST'])
def signup() : 
    return authentication.register_user()



@app.route('/login', methods=['POST'])
def login(): 
    return authentication.login()

@app.route('/logout', methods=['GET'])
def logout(): 
    return authentication.logout()


@app.route('/order', methods=['POST'])
def order(): 
    return product_controller.order()



if __name__ == '__main__':
    app.run(debug=True, port=5000)



