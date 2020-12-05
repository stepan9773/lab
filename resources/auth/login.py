from http import HTTPStatus

from flask import flash
from flask import request
from flask_login import login_user
from werkzeug.security import check_password_hash

from auth.auth import auth
from app import User


@auth.route('/user', methods=['POST'])
def login():
    data = request.get_json()
    password = data['password']
    name = data["username"]

    user = User.query.filter_by(username=name).first()
    if not user or not (user.password == password):
        flash("wrong password or email ")
        return "bed"

    login_user(user)

    return f"hello"
