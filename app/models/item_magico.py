from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base
import enum

class TipoItemEnum(str, enum.Enum):
    ARMA = "Arma"
    ARMADURA = "Armadura"
    AMULETO = "Amuleto"

class ItemMagico(Base):
    __tablename__ = "itens_magicos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    tipo = Column(Enum(TipoItemEnum))
    forca = Column(Integer)
    defesa = Column(Integer)
    personagem_id = Column(Integer, ForeignKey("personagens.id"))

    personagem = relationship("Personagem", back_populates="itens_magicos")
