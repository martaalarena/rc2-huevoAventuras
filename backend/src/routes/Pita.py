from flask import Blueprint, jsonify

#Models
from models.PitaModel import PitaModel

main = Blueprint('pita_blueprint', __name__)

@main.route('/')
def get_pitas():
    try:
            pitas=PitaModel.get_pitas()
            return jsonify(pitas)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id>')    
def get_pita(id):
    try:
            pita=PitaModel.get_pita(id)
            if pita != None:
                return jsonify(pita)
            else:
                return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500