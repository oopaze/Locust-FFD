from typing import List

from fastapi import APIRouter

from .models import Pessoa
from .schemas import PessoaSchema, PessoaReadSchema
from app.settings.db import session as db


route = APIRouter()

@route.get('/', response_model=List[PessoaReadSchema])
async def get_pessoas() -> List[PessoaReadSchema]:
    """Mostra todas as pessoas no banco"""
    data = db.query(Pessoa).all()
    return data


@route.post('/', response_model=PessoaSchema)
async def add_pessoa(pessoa: PessoaSchema) -> PessoaSchema:
    """Adiciona pessoa"""
    new_pessoa = Pessoa(**pessoa.__dict__)
    
    db.add(new_pessoa)
    db.commit()

    return pessoa