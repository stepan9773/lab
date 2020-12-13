import sqlalchemy as sqlalchemy

from flask_restful import Resource;

import app
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity,
)
from flask import jsonify
from app import User
class SmokeResources(Resource):
    """
    GET endpoint handler to test the process
    """

    @jwt_required
    def get(self):
        """
        Returns (str): Test message, SQLAlchemy version, and Hello :)
        """
        current_user = get_jwt_identity()
        curent = User.query.filter_by(username = current_user).first()
        return \
            f"""USER {curent.username}  {curent.password}
            Hello, Student! SQLAlchemy works just fine, and it's version is: {sqlalchemy.__version__}
            Database connection is OK, and it's array is: {app.db.ARRAY}
            """, 200
