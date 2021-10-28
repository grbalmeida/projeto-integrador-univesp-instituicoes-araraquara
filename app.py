from flask import Flask, render_template, request
from datetime import datetime

from http_clients.categoria_http_client import CategoriaHttpClient
from http_clients.img_http_client import ImgHttpClient
from http_clients.instituicao_http_client import InstituicaoHttpClient

app = Flask(__name__)

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@app.route("/home")
@app.route("/")
def home():
    img_client = ImgHttpClient()
    imgs = img_client.obter_imgs()

    return render_template ("home.html", imgs = imgs, mostrar_categorias = False, active_tab="home")

@app.route("/instituicoes")
def instituicoes():

    nome = request.args.get('nome')
    categoria_id = request.args.get('categoria_id')

    categoria_client = CategoriaHttpClient()
    instituicao_client = InstituicaoHttpClient()

    instituicoes = instituicao_client.obter_instituicoes(nome, categoria_id)
    categorias = categoria_client.obter_categorias()
    
    return render_template(
        "instituicoes.html", instituicoes = instituicoes, categorias = categorias, mostrar_categorias = True, nome=nome, active_tab="instituicoes")

if __name__ == "__main__":
    app.run(debug=True)