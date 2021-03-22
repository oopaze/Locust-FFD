from marshmallow_sqlalchemy import ModelSchema
from .models import Pessoa


class PessoaSchema(ModelSchema):
    class Meta:
        model = Pessoa