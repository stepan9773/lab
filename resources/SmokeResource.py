import sqlalchemy as sqlalchemy

from flask_restful import Resource;

import app
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity,
)
from http import HTTPStatus
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
        return 200
