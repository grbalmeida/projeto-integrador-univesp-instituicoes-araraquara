from flask import Flask, redirect, url_for, render_template, request, session
import sqlite3

app = Flask(__name__)

def db_connection():
    conn = None
    conn = sqlite3.connect("instituicoes.db")

@app.route("/home")
@app.route("/")
def home():
    return render_template ("home.html")

@app.route("/instituicoes")
def instituicoes():
    return render_template("instituicoes.html")

if __name__ == "__main__":
    app.run(debug=True)