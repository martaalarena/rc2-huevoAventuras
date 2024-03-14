from flask import Flask

from config import config

from routes import Pita

app = Flask(__name__)

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_blueprint(Pita.main, url_prefix='/api/pitas')
    app.run()