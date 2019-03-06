import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):


    parser = reqparse.RequestParser()


    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )


    def post(self):

        data = UserRegister.parser.parse_args()


        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # if UserModel.find_by_username(data['username']):
        #     return {"message":"A user with that username already exists"}, 400
        #
        # query = "INSERT INTO users VALUES (NULL, ?, ?)"
        # cursor.execute(query, (data['username'], data['password']))
        # connection.commit()
        # connection.close()
        #
        # return {"message": "User created successfully."}, 201

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        # **unpacking
        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201



