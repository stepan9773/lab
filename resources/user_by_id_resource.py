from flask_restful import Resource

from flask_restful import Resource

from app import User, Rights
from app import db
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

class UserByIDRasource(Resource):

    @jwt_required
    def get(self, id):
        current_user_name = get_jwt_identity()
        current_user = User.query.filter_by(username=current_user_name).first()
        user = User.query.filter_by(id=id).first()
        return {
            "id": id,
            "username": user.username,
            "password": user.password
        }
