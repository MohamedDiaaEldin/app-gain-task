from models.user import User
from database import db
from flask import request

def add_user():
    user  = User(username='moddhddamed', email='mdiaa@dd.com', address='dd', addressTwo='dd')
    print(request.get_json().get('username'))
    db.session.add(user)
    db.session.commit()
    return 'hello world'