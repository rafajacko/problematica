## iniciar o projeto 
  python -m venv venv 
  venv\Scripts\activate
---
## instale as dependências (arquivo gerado utilizando o comando pip install -r requirements.txt)
  pip install -r requirements.txt
---
## rodar o projeto 
  uvicorn main:app --reload
---
Rota do Swagger
  http://localhost:8000/docs
  
