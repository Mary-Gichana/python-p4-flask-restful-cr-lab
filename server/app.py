#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Plants(Resource):
    def get(self):
        '''GET /plants - Return a list of all plants'''
        plants = Plant.query.all()
        response = [plant.to_dict() for plant in plants]
        return make_response(jsonify(response), 200)

    def post(self):
        '''POST /plants - Create a new plant'''
        data = request.get_json()
        new_plant = Plant(
            name=data['name'],
            image=data['image'],
            price=data['price']
        )
        db.session.add(new_plant)
        db.session.commit()

        response_dict = new_plant.to_dict()
        return make_response(jsonify(response_dict), 201)


class PlantByID(Resource):
    def get(self, id):
        '''GET /plants/<int:id> - Return a specific plant by ID'''
        plant = db.session.get(Plant, id)  
        if plant is None:
            return make_response(jsonify({"error": "Plant not found"}), 404)
        response_dict = plant.to_dict()
        return make_response(jsonify(response_dict), 200)



# Add the resources to the API
api.add_resource(Plants, '/plants')
api.add_resource(PlantByID, '/plants/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
