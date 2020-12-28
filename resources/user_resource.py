from flask_restful import Resource

from app import User,Rights
from flask_jwt_extended import get_jwt_identity, jwt_required


class UserRasource(Resource):

    @jwt_required
    def get(self):
        current_user_name = get_jwt_identity()
        current_user = User.query.filter_by(username=current_user_name).first()
        print(current_user_name)
        users = User.query.all()
        response_dict = {}
        for user in users:
            response_dict[user.id] = {"username": user.username,
                                      "password": user.password}

        return response_dict
