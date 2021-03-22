from datetime import timedelta
from pathlib import Path


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "minha namorada é gata"

    
class Development(Config):
    ENV = 'development'
    DEBUG = True
    BASE_DIR = Path(__file__).resolve().parent.parent
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + str(BASE_DIR / 'storage.db')