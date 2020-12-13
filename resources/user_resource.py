from flask_restful import Resource

from app import User,Rights
from flask_jwt_extended import get_jwt_identity, jwt_required


class UserRasource(Resource):

    @jwt_required
    def get(self):
        current_user_name = get_jwt_identity()
        current_user = User.query.filter_by(username=current_user_name).first()
        print(current_user_name)
        if Rights.query.filter_by(user_id=current_user.id).first() is None:
            return "you not have any admin rights"
        if not Rights.query.filter_by(user_id=current_user.id).first().admin  and not current_user.username == 'admin':
            return "you not had rights for this request"
        users = User.query.all()
        if not users:
            return "No users exist", 404
        response_dict = {}
        for user in users:
            response_dict[user.id] = {"username": user.username,
                                      "password": user.password}

        return response_dict
