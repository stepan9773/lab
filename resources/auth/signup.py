from flask import request
from werkzeug.security import generate_password_hash

from app import db
from auth.auth import auth
from app import User


@auth.route('/user', methods={'PUT'})
def signup():
    data = request.get_json()
    name = data['username']
    password = data['password']


    user = User.query.filter_by(username=name).first()
    if user:
        return "this user already registered"

    new_user = User(username=name, password=password)
    db.session.add(new_user)
    db.session.commit()
    return f"hello {new_user.username}"
