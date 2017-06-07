from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store
from resources.annonce import Annonce, AnnonceList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vutoatbranlozc:895a4b073925044c3f7c152ae135d665c18fadd20a7fae30b9581edb5c4786e6@ec2-54-217-222-254.eu-west-1.compute.amazonaws.com:5432/dbmgsggj5eljl1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Annonce, '/annonce/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(AnnonceList, '/annonces')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
