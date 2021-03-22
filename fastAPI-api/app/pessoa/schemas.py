from pydantic import BaseModel, constr
from datetime import date
from typing import Optional


class PessoaSchema(BaseModel):
    nome: constr(max_length=50)
    genero: constr(max_length=50)
    interesse: constr(max_length=50)
    data_nascimento: Optional[date] = None

    class Config: 
        orm_mode = True


class PessoaReadSchema(BaseModel):
    id: Optional[int]
    nome: constr(max_length=50)
    genero: constr(max_length=50)
    interesse: constr(max_length=50)
    data_nascimento: Optional[date] = None

    class Config: 
        orm_mode = True