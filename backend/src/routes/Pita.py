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