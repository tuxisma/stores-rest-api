from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

#importing two methods from security.py
from security import authenticate, identity
#Importing class(UserRegister) from user.py
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

# Resources is thing that api can return , create, delete and so on
# Resource are usually mapped into databases tables as well.


#Config the api
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

#if you run the script without this decorator, the db will be created
#but you won't be able to put the table there
# with this decorator and method the table will be created
@app.before_first_request
def create_table():
    db.create_all()

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')  #This is my endpoint, this the way how to be access
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True) 


