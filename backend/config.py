# Importa a classe Flask do módulo flask para criar a aplicação web
from flask import Flask

# Importa a classe SQLAlchemy do módulo flask_sqlalchemy para manipulação do banco de dados
from flask_sqlalchemy import SQLAlchemy

# Importa a função CORS do módulo flask_cors para habilitar o Cross-Origin Resource Sharing
from flask_cors import CORS

# Cria uma instância do aplicativo Flask, que será a base para nossa aplicação web
# A instância de Flask é o núcleo da aplicação, onde definiremos configurações e rotas
app = Flask(__name__)

# Habilita o Cross-Origin Resource Sharing (CORS) na aplicação
# Isso permite que o aplicativo aceite requisições de outros domínios, o que é útil
# para interações entre o frontend e a API backend em domínios diferentes
CORS(app)

# Configura o URI do banco de dados na aplicação para usar um banco de dados SQLite
# Aqui, "sqlite:///mydatabase.db" indica que estamos usando o SQLite como banco de dados,
# e que o arquivo de banco de dados será chamado "mydatabase.db" (criado na raiz do projeto)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"

# Desativa o rastreamento de modificações do SQLAlchemy
# SQLALCHEMY_TRACK_MODIFICATIONS monitora todas as mudanças nos objetos do banco de dados
# para sinalizar eventos, mas isso pode consumir muita memória, então definimos como False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Cria uma instância de SQLAlchemy, que é a interface ORM (Object-Relational Mapping)
# Essa instância é responsável por interagir com o banco de dados, gerenciar modelos,
# tabelas e executar queries no banco de dados configurado acima
db = SQLAlchemy(app)
