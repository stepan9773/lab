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

    def post(self):
        data = request.get_json()
        password = data['password']
        username = data['username']

        user = User.query.filter_by(username=username).first()
        if not user or not (user.password == password):
            return "wrong password or user name", HTTPStatus.BAD_REQUEST
        login_user(user)
        return f"hello {user.username}"

    def put(self):
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
