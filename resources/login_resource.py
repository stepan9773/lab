
from flask_restful import Resource
from flask import jsonify,request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from werkzeug.security import check_password_hash
from app import User

class LoginResource(Resource):
    def post(self):
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        data = request.get_json()
        username = data["username"]
        password = data["password"]
        if not username:
            return jsonify({"msg": "Missing username parameter"}), 400
        if not password:
            return jsonify({"msg": "Missing password parameter"}), 400
        user = User.query.filter_by(username=username).first()
        if user is None:
            return "Bad username or password", 401

        if not check_password_hash(user.password, password):
            return "wrong password "
        # Identity can be any data that is json serializable
        access_token = create_access_token(identity=username, expires_delta=False)
        return str(access_token), 200

