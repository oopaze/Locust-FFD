
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from pathlib import Path


#The type and the name of our db
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
SQLALCHEMY_DATABASE_URL = 'sqlite:////' + str(BASE_DIR / 'storage.db')

#Configuring our db to a local sqlite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#Creating a session to mess edit ourt sqlite database
session = Session(autocommit=False, autoflush=False, bind=engine)

#Instanciating our mother model class
Model = declarative_base()