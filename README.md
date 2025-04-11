Crie e ative o ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate

Instale as dependências
```bash
pip install -r requirements.txt

Rode o servidor
```bash
uvicorn app.main:app --reload

Rota do Swagger
```bash
http://127.0.0.1:8000/docs