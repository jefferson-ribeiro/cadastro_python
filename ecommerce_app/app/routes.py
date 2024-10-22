from app import app
from flask import render_template, request

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cliente')
def cliente():
    return render_template('cliente_form.html')

@app.route('/produto')
def produto():
    return render_template('produto_form.html')

@app.route('/pedido')
def pedido():
    return render_template('pedido_form.html')
