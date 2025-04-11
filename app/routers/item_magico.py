from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.item_magico import ItemMagicoCreate, ItemMagicoResponse
from app.models.item_magico import ItemMagico, TipoItemEnum
from app.models.personagem import Personagem
from app.database.database import get_db

router = APIRouter(prefix="/itens", tags=["Itens Mágicos"])

@router.post("/", response_model=ItemMagicoResponse)
def create_item(item: ItemMagicoCreate, db: Session = Depends(get_db)):
    if item.forca == 0 and item.defesa == 0:
        raise HTTPException(status_code=400, detail="não podem ter F/D = 0")
    if item.tipo == TipoItemEnum.ARMA and item.defesa != 0:
        raise HTTPException(status_code=400, detail=" 0 de defesa")
    if item.tipo == TipoItemEnum.ARMADURA and item.forca != 0:
        raise HTTPException(status_code=400, detail="0 de força")
    if item.forca > 10 or item.defesa > 10:
        raise HTTPException(status_code=400, detail="Limite atingido")
    db_item = ItemMagico(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=List[ItemMagicoResponse])
def list_itens(db: Session = Depends(get_db)):
    return db.query(ItemMagico).all()

@router.get("/{item_id}", response_model=ItemMagicoResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemMagico).filter(ItemMagico.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item

@router.post("/{item_id}/personagem/{personagem_id}")
def add_item_to_personagem(item_id: int, personagem_id: int, db: Session = Depends(get_db)):
    personagem = db.query(Personagem).filter(Personagem.id == personagem_id).first()
    if not personagem:
        raise HTTPException(status_code=404, detail="Personagem não encontrado")
    item = db.query(ItemMagico).filter(ItemMagico.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    if item.tipo == TipoItemEnum.AMULETO:
        amuleto_existente = db.query(ItemMagico).filter(
            ItemMagico.personagem_id == personagem_id,
            ItemMagico.tipo == TipoItemEnum.AMULETO
        ).first()
        if amuleto_existente:
            raise HTTPException(status_code=400, detail="já possui amuleto equipado")
    item.personagem_id = personagem_id
    db.commit()
    return {"ok": True}

@router.get("/personagem/{personagem_id}", response_model=List[ItemMagicoResponse])
def list_itens_personagem(personagem_id: int, db: Session = Depends(get_db)):
    return db.query(ItemMagico).filter(ItemMagico.personagem_id == personagem_id).all()

@router.delete("/{item_id}/personagem")
def remove_item_from_personagem(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemMagico).filter(ItemMagico.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    item.personagem_id = None
    db.commit()
    return {"ok": True}

@router.get("/personagem/{personagem_id}/amuleto", response_model=ItemMagicoResponse)
def get_amuleto(personagem_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemMagico).filter(
        ItemMagico.personagem_id == personagem_id,
        ItemMagico.tipo == TipoItemEnum.AMULETO
    ).first()
    if not item:
        raise HTTPException(status_code=404, detail="Amuleto não encontrado")
    return item
