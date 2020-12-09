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
    if len(password) < 4:
        return "passwor must be longer then 4 charscters",404
    if len(name) < 4:
        return "your len of name too short ", 404
    user = User.query.filter_by(username=name).first()
    if user:
        return "This user already exist", 404

    new_user = User(username=name, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()

    return "create sucssesfull", 200