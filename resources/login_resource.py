
from flask_restful import Resource
from flask import request
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from app import User
from http import HTTPStatus


class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        user = User.query.filter_by(username=username).first()
        if user is None:
            return HTTPStatus.BAD_REQUEST
        if not check_password_hash(user.password, password):
            return 401
        access_token = create_access_token(identity=username, expires_delta=False)
        return str(access_token), 200

