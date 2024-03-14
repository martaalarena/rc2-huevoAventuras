from flask import Blueprint, jsonify, request

#Models
# from models.PitaRentingModel import PitaRentingModel

main = Blueprint('pitarentings_blueprint', __name__)

@main.route('/add', methods=['POST'])
def add_pita():
    try:
        pick_up_date=request.json['pick_up_date']
        return_date=request.json['return_date']


    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
