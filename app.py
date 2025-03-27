from flask import Flask, jsonify, request
from Previsao.previsaoEmocao import preverListaChamados

app = Flask(__name__)

@app.route('/prever', methods=['POST'])
def prever_emocoes():
    try:
        chamados = request.json["chamados"]
        resultados = preverListaChamados(chamados)
        
        return jsonify({
            "status": "success",
            "chamados": [
                {
                    "chamadoId": c["chamadoId"],
                    "descricao": c["descricao"],
                    "emocao": r["emocao"]
                }
                for c, r in zip(chamados, resultados)
            ]
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(port=8080, debug=True, host='0.0.0.0')  # Adicionei host='0.0.0.0'