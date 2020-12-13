from http import HTTPStatus

from flask import request, jsonify
from flask_login import login_user
from werkzeug.security import check_password_hash

from app import User
from auth.auth import auth

"""
@auth.route('/user', methods=['POST'])
def login():
    data = request.get_json()
    password = data['password']
    name = data["username"]

    user = User.query.filter_by(username=name).first()
    if not user and not check_password_hash(user.password, password):
        return "you write bad password or user name", HTTPStatus.BAD_REQUEST

    login_user(user)

    return {
        "user_id": user.id
    }
"""

