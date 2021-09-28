from flask import Flask, redirect, url_for, render_template, session
import requests
import json

app = Flask(__name__)

def db_connection():
    conn = None

@app.route("/home")
@app.route("/")
def home():
    imgs = requests.get("http://localhost:3000/api/imgs")
    print(json.loads(imgs.content))
    return render_template ("home.html", imgs = json.loads(imgs.content))

@app.route("/instituicoes")
def instituicoes():
    instituicoes = requests.get("http://localhost:3000/api/instituicoes")
    return render_template("instituicoes.html", instituicoes = json.loads(instituicoes.content))

if __name__ == "__main__":
    app.run(debug=True)