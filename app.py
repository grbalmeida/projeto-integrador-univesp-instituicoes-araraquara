from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os
from datetime import datetime

from http_clients.categoria_http_client import CategoriaHttpClient
from http_clients.img_http_client import ImgHttpClient
from http_clients.instituicao_http_client import InstituicaoHttpClient

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": os.environ.get('MAIL_SERVER'),
    "MAIL_PORT": os.environ.get('MAIL_PORT'),
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ.get('MAIL_USERNAME'),
    "MAIL_PASSWORD": os.environ.get('MAIL_PASSWORD')
}

app.config.update(mail_settings)
mail = Mail(app)

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@app.route("/home")
@app.route("/")
def home():
    img_client = ImgHttpClient()
    imgs = img_client.obter_imgs()

    return render_template ("home.html", imgs = imgs, mostrar_categorias = False, active_tab="home")

@app.route("/contato")
def contato():
    return render_template("contato.html", mostrar_categorias = False, active_tab="contato")

@app.route("/contato-envio", methods=['POST'])
def contato_envio():
    nome = request.form['nome']
    email = request.form['email']
    assunto = request.form['assunto']
    mensagem = request.form['mensagem']

    # Lógica email aqui

    with app.app_context():
        body = f'Nome: {nome}\r\n'
        body += f'E-mail: {email}\r\n\r\n'

        body += f'Mensagem: {mensagem}'
        msg = Message(subject=assunto, sender=email, recipients=[mail_settings['MAIL_USERNAME']], body=body)
        mail.send(msg)

    mensagem_sucesso = 'E-mail enviado com sucesso!'

    return render_template("contato.html", mostrar_categorias = False, active_tab="contato", mensagem_sucesso=mensagem_sucesso)

@app.route("/instituicoes")
def instituicoes():

    nome = request.args.get('nome')
    categoria_id = request.args.get('categoria_id')

    categoria_client = CategoriaHttpClient()
    instituicao_client = InstituicaoHttpClient()

    result = instituicao_client.obter_instituicoes(nome, categoria_id)
    instituicoes = result['instituicoes']
    categoria = result['categoria']
    categorias = categoria_client.obter_categorias()
    
    return render_template(
        "instituicoes.html",
        instituicoes = instituicoes,
        categorias = categorias,
        mostrar_categorias = True,
        nome=nome,
        categoria = categoria,
        active_tab="instituicoes")

if __name__ == "__main__":
    app.run(debug=True)