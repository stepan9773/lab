import sqlalchemy as sqlalchemy
import jsonify
from flask_restful import Resource, request;
import app



class SmokeResources(Resource):
    """
    GET endpoint handler to test the process
    """

    def get(self):
        """
        Returns (str): Test message, SQLAlchemy version, and Hello :)
        """
        # stud = app.Students(
        #     rating = 5
        #     , first_name = 'Joseph'
        #     , last_name = 'Antonio'
        # )
        # app.db.session.add(stud)
        # app.db.session.commit()
        return \
            f"""
            Hello, Student! SQLAlchemy works just fine, and it's version is: {sqlalchemy.__version__} Database connection is OK, and it's array is: {app.db.ARRAY}
            """, 200;


    # def post(self):
    #     data = app.Students.query.filter_by(student_id=2).first()
    #     return jsonify(data)

        '''
        
        data = request.get_json()
        stud = {
            'student_id' : data['student_id']
            , 'grade' : data['grade']
            , 'comments' : data['comments']
        }
        '''

