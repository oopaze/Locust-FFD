from app.settings.db import db


class Pessoa(db.Model):
    __tablename__ = 'pessoas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    data_nascimento = db.Column(db.Date, nullable=True)
    genero = db.Column(db.String(50))
    interesse = db.Column(db.String(50))

    def __init__(self, nome, genero, interesse, data_nascimento = None):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.genero = genero
        self.interesse = interesse