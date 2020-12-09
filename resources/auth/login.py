from http import HTTPStatus

from flask import flash
from flask import request
from flask_login import login_user
from werkzeug.security import check_password_hash
from http import HTTPStatus
from auth.auth import auth
from app import User


@auth.route('/user', methods=['POST'])
def login():
    data = request.get_json()
    password = data['password']
    name = data["username"]

    user = User.query.filter_by(username=name).first()
    if not user and not check_password_hash(user.password, password):
        return "you write bad password or user name",HTTPStatus.BAD_REQUEST

    login_user(user)

    return f"hello"
