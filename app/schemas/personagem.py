from pydantic import BaseModel
from typing import Optional, List
from app.schemas.item_magico import ItemMagicoResponse
from app.models.personagem import ClasseEnum

class PersonagemBase(BaseModel):
    nome: str
    nome_aventureiro: str
    classe: ClasseEnum
    level: int
    forca_base: int
    defesa_base: int

class PersonagemCreate(PersonagemBase):
    pass

class PersonagemUpdateNome(BaseModel):
    nome: str

class PersonagemResponse(PersonagemBase):
    id: int
    itens_magicos: List[ItemMagicoResponse] = []

    class Config:
        orm_mode = True
