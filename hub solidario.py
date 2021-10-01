from flask import Flask, redirect, url_for, render_template, session, request
import requests
import json

# from requests.api import request

app = Flask(__name__)

def db_connection():
    conn = None

@app.route("/home")
@app.route("/")
def home():
    imgs = requests.get("http://localhost:3000/api/imgs")
    print(json.loads(imgs.content))
    return render_template ("home.html", imgs = json.loads(imgs.content), mostrar_categorias = False)

@app.route("/instituicoes")
def instituicoes():

    nome = request.args.get('nome')

    if not nome:
        instituicoes = json.loads(requests.get("http://localhost:3000/api/instituicoes").content)
    else:
        instituicoes = json.loads(requests.get("http://localhost:3000/api/instituicoes?name_like=" + nome).content)
    
    categorias = json.loads(requests.get("http://localhost:3000/api/categorias").content)
    
    return render_template("instituicoes.html", instituicoes = instituicoes, categorias = categorias, mostrar_categorias = True, nome=nome)

@app.route("/instituicoes/<categoria_id>")
def instituicoes_id(categoria_id):
    categorias = json.loads(requests.get("http://localhost:3000/api/categorias").content)
    instituicoes = json.loads(requests.get("http://localhost:3000/api/instituicoes?categoria_id=" + categoria_id).content)
    return render_template("instituicoes.html", instituicoes = instituicoes, categorias = categorias, mostrar_categorias = True)

# @app.route("/instituicoes?nome=<nome>")
# def instituicoes_nome(nome):
#     categorias = json.loads(requests.get("http://localhost:3000/api/categorias").content)
#     instituicoes = json.loads(requests.get("http://localhost:3000/api/instituicoes?name_like=" + nome).content)
#     print (nome)
#     return render_template("instituicoes.html", instituicoes = instituicoes, categorias = categorias, mostrar_categorias = True)

if __name__ == "__main__":
    app.run(debug=True)