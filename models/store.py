from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # allows a store to see which items are in the items table
    # here we are using lazy='dinamic'
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        #if you put .all(self.items.all()) you must set lazy='dynamic'
        # in the relationship
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

        # if you want to use this line, delete lazy='dynamic'
        # return {'name': self.name, 'items': [item.json() for item in self.items]}

    @classmethod
    def find_by_name(cls, name):

        #using SQLAlchemy
        # SELECT * FROM items WHERE name=name LIMIT 1
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

