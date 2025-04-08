from flask import Flask
from config import Config
from database import db
from routes.personagens import bp_personagens
from routes.itens_magicos import bp_itens

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(bp_personagens)
app.register_blueprint(bp_itens)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
