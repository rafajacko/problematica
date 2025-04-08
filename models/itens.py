from database import db

class ItemMagico(db.Model):
    __tablename__ = 'itens'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(20), nullable=False) 
    forca = db.Column(db.Integer, nullable=False)
    defesa = db.Column(db.Integer, nullable=False)

    personagem_id = db.Column(db.Integer, db.ForeignKey('personagens.id'))

    def __init__(self, nome, tipo, forca, defesa, personagem_id=None):
        if tipo == 'Arma':
            defesa = 0
        elif tipo == 'Armadura':
            forca = 0

        if forca == 0 and defesa == 0:
            raise ValueError("Item não pode ter Força e Defesa iguais a zero.")

        if forca > 10 or defesa > 10:
            raise ValueError("Força e Defesa não podem ser maiores que 10.")

        self.nome = nome
        self.tipo = tipo
        self.forca = forca
        self.defesa = defesa
        self.personagem_id = personagem_id
