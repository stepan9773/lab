import sqlalchemy as sqlalchemy
import jsonify
from flask import send_from_directory
from flask_restful import Resource, request;
import app


class SendFromDirectorySwagger(Resource):
    """
    GET endpoint handler for swagger
    """

    def get(self, path):
        """
        Returns some swagger shit
        """
        return send_from_directory('static', path);



