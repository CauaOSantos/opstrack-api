
from flask import Flask, jsonify

app = Flask(__name__)

VERSAO = "1.0.0"


@app.route("/")
def home():
    return jsonify({
        "servico": "OpsTrack API",
        "status": "online"
    })


@app.route("/status")
def status():
    return jsonify({
        "status": "ok"
    })


@app.route("/tickets")
def tickets():
    return jsonify({
        "tickets": [
            {
                "id": 1,
                "titulo": "Erro no login",
                "status": "aberto"
            },
            {
                "id": 2,
                "titulo": "Problema no sistema",
                "status": "em andamento"
            },
            {
                "id": 3,
                "titulo": "Solicitacao de acesso",
                "status": "fechado"
            }
        ]
    })


@app.route("/usuarios")
def usuarios():
    return jsonify({
        "usuarios": [
            {"id": 1, "nome": "Ana"},
            {"id": 2, "nome": "Carlos"}
        ]
    })


@app.route("/versao")
def versao():
    return jsonify({
        "versao": VERSAO
    })


if __name__ == "__main__":
    app.run(debug=True)
