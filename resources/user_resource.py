from http import HTTPStatus

from flask import request
from flask_restful import Resource
from flask_login import login_user
from app import User
from app import db


class UserRasource(Resource):

    def get(self):
        users = User.query.all()
        response_dict = {}
        for user in users:
            response_dict[user.id] = {"suername": user.username,
                                      "password": user.password}

        return response_dict

