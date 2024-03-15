from flask import Blueprint, jsonify, request

#Models
# from models.PitaWalkModel import PitaWalkModel

main = Blueprint('pitawalks_blueprint', __name__)


@main.route('/add', methods=['POST'])
def add_pitaWalk():
    try:
        pick_up_time=request.json['pick_up_time']
        return_time=request.json['return_time']

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500