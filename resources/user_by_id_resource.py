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
        if Rights.query.filter_by(user_id=current_user.id).first() is None:
            return "you not have any admin rights"
        if Rights.query.filter_by(user_id=current_user.id).first() is None and current_user_name != 'admin':
            return "you not had rights for this request"
        user = User.query.filter_by(id=id).first()
        if not user:
            return f"no user with id {id} ", 404
        return {
            "id": id,
            "username": user.username,
            "password": user.password
        }

    @jwt_required
    def delete(self, id):
        current_user_name = get_jwt_identity()
        current_user = User.query.filter_by(username=current_user_name).first()

        if Rights.query.filter_by(user_id=current_user.id).first() is not None or current_user_name == 'admin':
            return "you not had rights for this request"

        user = User.query.filter_by(id=id).first()
        if not user:
            return f"no user with id {id} ", 404
        name = user.username
        db.session.delete(user)
        db.session.commit()
        return f"user {name} delete"
