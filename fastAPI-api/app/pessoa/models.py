from sqlalchemy import Column, String, Integer, Date
from app.settings.db import Model


class Pessoa(Model):
    __tablename__ = 'pessoas'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    data_nascimento = Column(Date, nullable=True)
    genero = Column(String(50))
    interesse = Column(String(50))

    def __init__(self, nome, genero, interesse, data_nascimento=None, **kwargs):
        self.nome = nome
        self.genero = genero
        self.interesse = interesse
        self.data_nascimento = data_nascimento