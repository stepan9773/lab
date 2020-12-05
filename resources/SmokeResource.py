import sqlalchemy as sqlalchemy
from flask_restful import Resource;
from flask_login import current_user
import app


class SmokeResources(Resource):
    """
    GET endpoint handler to test the process
    """
    def get(self):
        """
        Returns (str): Test message, SQLAlchemy version, and Hello :)
        """
        return \
            f"""USER {current_user}
            Hello, Student! SQLAlchemy works just fine, and it's version is: {sqlalchemy.__version__}
            Database connection is OK, and it's array is: {app.db.ARRAY}
            """, 200
