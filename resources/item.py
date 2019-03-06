from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

#Defining our resource
#Every resource has to be a class
class Item(Resource):

    #added this 2 lines (parser) due to this criteria will be in 'post' and 'put'
    #notice this properties belong to the Item class, so that's why we need to apply Item.parser.parse_args()
    #see 'data = Item.parser.parse_args()' in post method, same with 'put' method
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item needs a store id."
                        )


    @jwt_required()
    #method that the resource is going to accept(get), also could be (post, delete, etc.)
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item
        #doing the same below:
        #commenting the next lines due to now we are using a database
        # item = next(filter(lambda x: x['name'] == name, items), None)
        # return {'item': item}, 200 if item else 404

        item = ItemModel.find_by_name(name)
        if item:
            #we have created a json method into the model 'resources/item'
            return item.json()
        return {'message': 'Item not found'}, 404

    @jwt_required()
    def post(self, name):
        # if next(filter(lambda x: x['name'] == name, items), None):
        #     return {'message': "An item with name '{}' already exists.".format(name)}, 400

        # if Item.find_by_name(name):
        # or
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400


        data = Item.parser.parse_args()
        # item = ItemModel(name, data['price'], data['store_id'])
        # or
        item = ItemModel(name, **data)


        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    @jwt_required()
    def delete(self, name):

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "DELETE FROM items WHERE name = ?"
        # cursor.execute(query, (name,))
        #
        # connection.commit()
        # connection.close()
        #
        # return {'message': 'Item deleted'}
        # <<<code before

        # code now>>>>
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'Item deleted'}

    @jwt_required()
    def put(self, name):

        # data = Item.parser.parse_args()
        #
        # item = ItemModel.find_by_name(name)
        #
        # updated_item = ItemModel(name, data['price'])
        #
        # if item is None:
        #     try:
        #         updated_item.insert()
        #     except:
        #         return {"message": "An error occurred inserting the item."}, 500
        # else:
        #     try:
        #         updated_item.update()
        #     except:
        #         return {"message": "An error occurred updating the item."}, 500
        #
        # # we have created a json method into the model 'resources/item'
        # return updated_item.json()
        # <<<code before

        # code now>>>>
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            # item = ItemModel(name, data['price'], data['store_id'])
            # or
            item = ItemModel(name, **data)
        else:
            item.price = data['price']

        item.save_to_db()
        return item.json()


class ItemList(Resource):
    @jwt_required()
    def get(self):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM items"
        # result = cursor.execute(query)
        # items = []
        # for row in result:
        #     items.append({'name': row[1], 'price': row[2]})
        #
        #
        # connection.close()

        # return {'items': items}, 201
        # <<<code before

        # code now>>>>

        # using list comprehension
        return {'items': [x.json() for x in ItemModel.query.all()]}


        #using lambda function
        # return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}

