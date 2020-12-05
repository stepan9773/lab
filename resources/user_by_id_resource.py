from http import HTTPStatus

from flask import request
from flask_restful import Resource

from app import User
from app import db


class UserByIDRasource(Resource):

    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return f"no user with id {id} "
        return {
            "id": id,
            "username": user.username,
            "password": user.password
        }

    def delete(self, id):

        user  = User.query.filter_by(id=id).first()
        if not user:
            return f"no user with id {id} "
        name = user.username
        db.session.delete(user)
        db.session.commit()
        return f"user {name} delete"
