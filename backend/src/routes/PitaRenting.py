from flask import Blueprint, jsonify, request

#Models
from models.entities.PitaRenting import PitaRenting
from models.PitaRentingModel import PitaRentingModel

main = Blueprint('pitarentings_blueprint', __name__)

@main.route('/add', methods=['POST'])
def add_pita():
    try:
        pick_up_date = request.json['pick_up_date']
        return_date = request.json['return_date']
        pita = PitaRenting(str(id),pick_up_date,return_date)

        affected_rows = PitaRentingModel.add_pita(pita)

        if affected_rows == 1:
            return jsonify(pita.id)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
