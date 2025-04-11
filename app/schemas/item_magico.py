from pydantic import BaseModel
from typing import Optional
from app.models.item_magico import TipoItemEnum

class ItemMagicoBase(BaseModel):
    nome: str
    tipo: TipoItemEnum
    forca: int
    defesa: int

class ItemMagicoCreate(ItemMagicoBase):
    pass

class ItemMagicoResponse(ItemMagicoBase):
    id: int
    personagem_id: Optional[int]

    class Config:
        orm_mode = True
