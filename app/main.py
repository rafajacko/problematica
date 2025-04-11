from fastapi import FastAPI
from app.database.database import Base, engine
from app.routers import personagem, item_magico

Base.metadata.create_all(bind=engine)

app = FastAPI(title="RPG Manager")

app.include_router(personagem.router)
app.include_router(item_magico.router)
