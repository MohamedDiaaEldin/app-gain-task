from crypt import methods
from flask import Flask
from flask_migrate import Migrate
from database import configure_with_database, db
# from models.user import User
from controllers.authentication import add_user

app = Flask(__name__)
app = configure_with_database(app)

@app.route('/' , methods=['POST'])
def index():
    # user  = User(username='mohamed', email='mdiaa@gmail.com', address='cairo', addressTwo='october')
    # db.session.add(user)
    # db.session.commit()
    # return 'Hello, World'
    return add_user()


if __name__ == '__main__':
    app.run(debug=True, port=5000)



