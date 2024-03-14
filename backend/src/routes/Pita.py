from flask import Blueprint, jsonify

main = Blueprint('pita_blueprint', __name__)

@main.route('/')
def get_pitas():
    return jsonify({'message': "hola"})