"""
Main Application Entry Point

This module initializes the Flask application and defines routes for user authentication and product ordering.

Routes:
    - /register (POST): Register a new user.
    - /login (POST): Log in an existing user.
    - /logout (GET): Log out the currently authenticated user.
    - /order (POST): Place an order for a product.

"""

from flask import Flask
from database import configure_with_database
from controllers import authentication, product_controller
from utilities.read_env import get_env

app = Flask(__name__)
app = configure_with_database(app)


@app.route('/', methods=['GET'])
def index(): 
    return 'ok'

@app.route('/register', methods=['POST'])
def signup():
    """
    Register a new user.

    Returns:
        Response: Success or error response.
    """
    return authentication.register_user()

@app.route('/login', methods=['POST'])
def login():
    """
    Log in an existing user.

    Returns:
        Response: Success or error response.
    """
    return authentication.login()

@app.route('/logout', methods=['GET'])
def logout():
    """
    Log out the currently authenticated user.

    Returns:
        Response: Success or error response.
    """
    return authentication.logout()

@app.route('/order', methods=['POST'])
def order():
    """
    Place an order for a product.

    Returns:
        Response: Success or error response.
    """
    return product_controller.order()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' , port= get_env('PORT') or 5000)
