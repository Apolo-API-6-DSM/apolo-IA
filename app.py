from flask import Flask, jsonify, request
from Previsao.previsaoEmocao import preverListaChamados

app = Flask(__name__)

# Rota para adicionar um novo item
@app.route('/prever', methods=['POST'])
def add_item():
    chamados = request.json["chamados"]
    listaChmadosPrevistos = preverListaChamados(chamados)
    return jsonify(listaChmadosPrevistos), 201

if __name__ == '__main__':
    app.run(debug=True, port=8080)