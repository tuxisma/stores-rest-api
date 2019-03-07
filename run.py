from app import app
from db import db

db.init_app(app)



#if you run the script without this decorator, the db will be created
#but you won't be able to put the table there
# with this decorator and method the table will be created
@app.before_first_request
def create_table():
  db.create_all()
