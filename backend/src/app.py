from flask import Flask

from config import config

from routes import Pita
from routes import PitaWalk
from routes import PitaRenting


app = Flask(__name__)

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_blueprint(Pita.main, url_prefix='/api/pitas')
    app.register_blueprint(PitaWalk.main, url_prefix='/api/pitawalks')
    app.register_blueprint(PitaRenting.main, url_prefix='/api/pitarentings')

    app.run()