
from flask_restful import Resource
from flask import jsonify,request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from werkzeug.security import check_password_hash
from app import User, Rights, db

class AdminResource(Resource):
    @jwt_required
    def post(self):
        data = request.get_json()
        username = data['username']
        admin = data['admin']

        current_user_name = get_jwt_identity()
        current_user = User.query.filter_by(username=current_user_name).first()
        print(current_user_name)
        if Rights.query.filter_by(user_id = current_user.id).first() is  None or not current_user_name == 'admin' :
            return "you not had rights for this request"
        new_current_user = User.query.filter_by(username=username).first()
        new_rights = Rights(user_id=new_current_user.id,admin=admin)
        db.session.add(new_rights)
        db.session.commit()

        return 200

