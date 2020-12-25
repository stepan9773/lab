
from flask_restful import Resource
from flask import jsonify,request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from werkzeug.security import check_password_hash
from app import User
from werkzeug.security import generate_password_hash
from app import db

class SignupResource(Resource):
    def post(self):
        data = request.get_json()
        name = data['username']
        password = data['password']

        user = User.query.filter_by(username=name).first()
        if user:
            return "This user already exist", 200

        new_user = User(username=name, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()

        return "create sucssesfull", 200
