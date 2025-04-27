from flask import Flask, jsonify, request
from Previsao.previsao import preverListaChamados
import requests
import logging
from Treinamento.PreProcessamento.eliminadorRuido import tornar_texto_legivel_humano

app = Flask(__name__)

NESTJS_URL = "http://localhost:3003/chamados/atualizar-emocoes"

logging.basicConfig(level=logging.INFO)


@app.route('/prever', methods=['POST'])
def prever_emocoes():
    try:
        chamados = request.json.get("chamados", [])

        if not chamados or not isinstance(chamados, list):
            logging.error("Nenhum chamado fornecido ou formato inválido.")
            return jsonify({
                "status": "error",
                "message": "Nenhum chamado fornecido ou formato inválido."
            }), 400

        logging.info(f"Recebidos {len(chamados)} chamados para previsão.")

        # Processar os chamados e prever emoção e tipo de chamado
        resultados = preverListaChamados(chamados)
        
        if not resultados:
            logging.error("Nenhum resultado foi gerado pela função preverListaChamados.")
            return jsonify({
                "status": "error",
                "message": "Nenhum resultado foi gerado pela função preverListaChamados."
            }), 500

        # Preparar o payload para envio ao NestJS
        payload = {"chamados": [
            {
                "chamadoId": c["chamadoId"],
                "descricao": c["descricao"],
                "emocao": r.get("emocao"),
                "tipoChamado": r.get("tipoChamado"),
                "sumarizacao":r.get("sumarizacao")
            }
            for c, r in zip(chamados, resultados)
        ]}
        logging.info(f"Resultado: {resultados[0]["sumarizacao"]}")
        logging.info(f"Payload: {payload['chamados'][0]["sumarizacao"]}")
        response = requests.post(NESTJS_URL, json=payload)

        # Verifica se os dados foram salvos com sucesso
        if response.status_code not in (200, 201):  
            logging.error(f"Erro ao enviar dados para o NestJS: {response.status_code} - {response.text}")
            return jsonify({
                "status": "error",
                "message": f"Erro ao enviar dados para o NestJS: {response.status_code} - {response.text}"
            }), response.status_code

        logging.info("Dados enviados com sucesso para o NestJS.")

        return jsonify({
            "status": "success",
            "message": "Dados processados e enviados com sucesso!",
            "chamados": payload["chamados"]
        })

    except Exception as e:
        logging.error(f"Erro interno do Flask: {str(e)}", exc_info=True)
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/prever/teste', methods=['POST'])
def prever_emocoes_teste():
    chamados = request.json.get("chamados", [])

    if not chamados or not isinstance(chamados, list):
        logging.error("Nenhum chamado fornecido ou formato inválido.")
        return jsonify({
            "status": "error",
            "message": "Nenhum chamado fornecido ou formato inválido."
        }), 400

    logging.info(f"Recebidos {len(chamados)} chamados para previsão.")

    # Processar os chamados e prever emoção e tipo de chamado
    resultados = preverListaChamados(chamados)

    return resultados

if __name__ == '__main__':
    app.run(port=8080, debug=True, host='0.0.0.0')
