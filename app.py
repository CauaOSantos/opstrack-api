from flask import Flask

app = Flask(__name__)

@app.route("/")
def status():
   return {'servico': 'OpsTrackAPI', 'status': 'up'}

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
    
@app.route("/quests")
def list_quests():
    quests = [
        {
            "id": "Q-101",
            "titulo": "Derrotar o Monstro do Memory Leak",
            "dificuldade": "Épica",
            "recompensa": {"xp": 1200, "gold": 300},
            "status": "Em Progresso"
        },
        {
            "id": "Q-102",
            "titulo": "Deploy na Sexta-feira sem Derrubar Produção",
            "dificuldade": "Lendária",
            "recompensa": {"xp": 3500, "gold": 1000},
            "status": "Disponível"
        },
        {
            "id": "Q-103",
            "titulo": "Limpeza das Tabelas Órfãs do Banco",
            "dificuldade": "Fácil",
            "recompensa": {"xp": 250, "gold": 50},
            "status": "Concluída"
        }
    ]
    return jsonify({"quests_ativas": quests, "total": len(quests)})
 
@app.route("/leaderboard")
def leaderboard():
    ranking = [
        {"posicao": 1, "membro": "Ana (Senior Mage)", "pontos_xp": 18450, "bugs_mortos": 89},
        {"posicao": 2, "membro": "DevMaster_99 (Paladin)", "pontos_xp": 14200, "bugs_mortos": 64},
        {"posicao": 3, "membro": "Carlos (Junior Rogue)", "pontos_xp": 9800, "bugs_mortos": 31}
    ]
    return jsonify({
        "temporada": "Sprint 2026.3",
        "ranking": ranking
    })

if __name__ == "__main__":
    app.run(debug=True)

