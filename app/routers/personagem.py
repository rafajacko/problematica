from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.personagem import PersonagemCreate, PersonagemResponse, PersonagemUpdateNome
from app.models.personagem import Personagem
from app.database.database import get_db
from app.models.personagem import ClasseEnum

router = APIRouter(prefix="/personagens", tags=["Personagens"])

@router.post("/", response_model=PersonagemResponse)
def create_personagem(personagem: PersonagemCreate, db: Session = Depends(get_db)):
    if personagem.forca_base + personagem.defesa_base > 10:
        raise HTTPException(status_code=400, detail="A soma de força e defesa não pode exceder 10.")
    db_personagem = Personagem(**personagem.dict())
    db.add(db_personagem)
    db.commit()
    db.refresh(db_personagem)
    return db_personagem

@router.get("/", response_model=List[PersonagemResponse])
def list_personagens(db: Session = Depends(get_db)):
    return db.query(Personagem).all()

@router.get("/{personagem_id}", response_model=PersonagemResponse)
def get_personagem(personagem_id: int, db: Session = Depends(get_db)):
    personagem = db.query(Personagem).filter(Personagem.id == personagem_id).first()
    if not personagem:
        raise HTTPException(status_code=404, detail="Personagem não encontrado")
    return personagem

@router.put("/{personagem_id}/nome", response_model=PersonagemResponse)
def update_nome(personagem_id: int, nome_data: PersonagemUpdateNome, db: Session = Depends(get_db)):
    personagem = db.query(Personagem).filter(Personagem.id == personagem_id).first()
    if not personagem:
        raise HTTPException(status_code=404, detail="Personagem não encontrado")
    personagem.nome = nome_data.nome
    db.commit()
    db.refresh(personagem)
    return personagem

@router.delete("/{personagem_id}")
def delete_personagem(personagem_id: int, db: Session = Depends(get_db)):
    personagem = db.query(Personagem).filter(Personagem.id == personagem_id).first()
    if not personagem:
        raise HTTPException(status_code=404, detail="Personagem não encontrado")
    db.delete(personagem)
    db.commit()
    return {"ok": True}
