from flask import Blueprint, jsonify, request


#Models
from models.entities.PitaRenting import PitaRenting
from models.PitaRentingModel import PitaRentingModel

main = Blueprint('pitarentings_blueprint', __name__)

@main.route('/add', methods=['POST'])
def add_pitaRenting():
    try:
        pick_up_date = request.json['pick_up_date']
        return_date = request.json['return_date']

        pitaRenting = PitaRenting(pick_up_date,return_date)

        affected_rows = PitaRentingModel.add_pitaRenting(pitaRenting)

        if affected_rows == 1:
            return jsonify(pitaRenting.id)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
