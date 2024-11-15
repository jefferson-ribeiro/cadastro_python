from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')

# Configurar a URI do banco de dados para SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{app.config['MYSQL_USER']}:{app.config['MYSQL_PASSWORD']}@{app.config['MYSQL_HOST']}/{app.config['MYSQL_DB']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar a instância do SQLAlchemy
db = SQLAlchemy(app)

from app import routes
