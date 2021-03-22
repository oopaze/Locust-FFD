from datetime import datetime

from flask import Blueprint, request, jsonify

from .schemas import PessoaSchema
from .models import Pessoa
from app.settings.db import db


pessoa = Blueprint('pessoa', __name__)


@pessoa.route('/', methods=['GET'])
def read_pessoa():
    pessoa_schema = PessoaSchema(many=True)
    pessoas = Pessoa.query.all()

    if pessoas:
        dados = pessoa_schema.dump(pessoas)
        return jsonify(dados), 200
    
    else:
        dados = {
            'message': 'Nenhuma pessoa registrada.'
        }
        return jsonify(dados), 404


@pessoa.route('/', methods=['POST'])
def create_pessoa():
    pessoa_schema = PessoaSchema()
    
    dados = request.json
    dados['data_nascimento'] = datetime.strptime(dados['data_nascimento'], '%Y-%m-%d')
    pessoa = Pessoa(**dados)

    db.session.add(pessoa)

    try:
        db.session.commit()

        dados = {}
        dados['pessoa'] = pessoa_schema.dump(pessoa)
        dados['message'] = 'Pessoa adicionada com sucesso.'
        return jsonify(dados), 201
    
    except ValueError:
        dados = {
            'message': 'Erro ao adicionar pessoa.'
        }
        return jsonify(dados), 400