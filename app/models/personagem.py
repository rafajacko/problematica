from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.database.database import Base
import enum

class ClasseEnum(str, enum.Enum):
    GUERREIRO = "Guerreiro"
    MAGO = "Mago"
    ARQUEIRO = "Arqueiro"
    LADINO = "Ladino"
    BARDO = "Bardo"

class Personagem(Base):
    __tablename__ = "personagens"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    nome_aventureiro = Column(String)
    classe = Column(Enum(ClasseEnum))
    level = Column(Integer)
    forca_base = Column(Integer)
    defesa_base = Column(Integer)

    itens_magicos = relationship("ItemMagico", back_populates="personagem")
