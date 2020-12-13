from flask_restful import Resource

from app import User


class UserRasource(Resource):

    def get(self):
        users = User.query.all()
        if not users:
            return "No users exist", 404
        response_dict = {}
        for user in users:
            response_dict[user.id] = {"suername": user.username,
                                      "password": user.password}

        return response_dict
