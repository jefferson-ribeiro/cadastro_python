import mysql.connector
from flask import Flask

app = Flask(__name__)
app.config.from_object('config.Config')

# Conectar ao banco de dados
db = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

from app import routes