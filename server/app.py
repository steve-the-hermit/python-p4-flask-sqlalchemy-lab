from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get(id)
    if animal:
        response = make_response(f'<h2>Animal: {animal.name}</h2>')
        return response
    else:
        return 'Animal not found', 404

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get(id)
    if zookeeper:
        response = make_response(f'<h2>Zookeeper: {zookeeper.name}</h2>')
        return response
    else:
        return 'Zookeeper not found', 404

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get(id)
    if enclosure:
        response = make_response(f'<h2>Enclosure: {enclosure.environment}</h2>')
        return response
    else:
        return 'Enclosure not found', 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)
