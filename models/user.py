from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    #adding "cls" to the class , because of @classmethod
    @classmethod
    def find_by_username(cls, username):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM users WHERE username=?"
        # #the only way to get data by username, is filter by a tuple: (username,)
        # result = cursor.execute(query, (username,))
        # #get the firt row
        # row = result.fetchone()
        #
        # if row:
        #     # user = User(row[0], row[1], row[2])
        #     # another way
        #     user = cls(*row)
        # else:
        #     user = None
        #
        # connection.close()
        # return user
        # <<<code before

        # code now>>>>
        #the first parameter is the column of the table and second one is the param into the 'find_by_username(cls, username)' function
        return cls.query.filter_by(username=username).first()



    #adding "cls" to the class , because of @classmethod
    @classmethod
    def find_by_id(cls, _id):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM users WHERE id=?"
        # #the only way to get data by username, is filter by a tuple: (username,)
        # result = cursor.execute(query, (_id,))
        # #get the firt row
        # row = result.fetchone()
        #
        # if row:
        #     # user = User(row[0], row[1], row[2])
        #     # another way
        #     user = cls(*row)
        # else:
        #     user = None
        #
        # connection.close()
        # return user
        # <<<code before

        # code now>>>>
        return cls.query.filter_by(id=_id).first()
