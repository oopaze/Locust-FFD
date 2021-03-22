from flask import Flask

from app.settings.db import configure_db
from app.settings.ma import configure_ma
from app.pessoa.routes import pessoa


def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Development')

    configure_db(app)
    configure_ma(app)

    app.register_blueprint(pessoa, url_prefix='/pessoa')

    return app