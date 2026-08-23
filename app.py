from flask import Flask

app = Flask(__name__)

@app.route("/")
def status():
   return {'servico': 'OpsTrackAPI', 'status': 'online'}

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/player/profile")
def player_profile():
    return jsonify({
        "nickname": "DevMaster_99",
        "classe": "Site Reliability Paladin",
        "level": 14,
        "xp": {"atual": 4850, "proximo_nivel": 6000},
        "mana": "85% (Cafeína)",
        "equipamentos": [
            {"item": "Teclado Mecânico Barulhento", "buff": "+15 Digitação Rápida"},
            {"item": "Monitor Ultrawide", "buff": "+20 Visão de Logs"}
        ]
    })

if __name__ == "__main__":
    app.run(debug=True)

