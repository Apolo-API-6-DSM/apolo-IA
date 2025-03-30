from PreProcessamento.preProcessamento import pre_processar
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import os


base_dir = os.getcwd()

tfidfEmocao = joblib.load(f'{base_dir}\\Treinamento\\Exportados\\emocao_vetorizador.pkl')
modeloEmocao= joblib.load(f'{base_dir}\\Treinamento\\Exportados\\modelo_emocao.pkl')

tfidfTipoChamado = joblib.load(f'{base_dir}\\Treinamento\\Exportados\\tipo_chamado_vetorizador.pkl')
modeloTipoChamado = joblib.load(f'{base_dir}\\Treinamento\\Exportados\\modelo_tipo_chamado.pkl')

def prever(texto, tfidf, modelo):
    # Pré-processar o texto
    texto_processado = pre_processar(texto)
    
    # Transformar o texto em vetores TF-IDF
    texto_vetorizado = tfidf.transform([texto_processado])
    
    # Fazer a previsão
    emocao = modelo.predict(texto_vetorizado)
    
    return emocao[0]

def preverListaChamados(chamados):
    chamados_previstos = []
    for chamado in chamados:
        emocao = prever(chamado["descricao"],tfidfEmocao, modeloEmocao)
        tipoChamado = prever(chamado["descricao"],tfidfTipoChamado, modeloTipoChamado)
        #tipoDocumento = preverTipoDocumento(chamado["descricao"])
        chamado_previsto = {
            "chamadoId":chamado["chamadoId"],
            "decricao":chamado["descricao"],
            "emocao":emocao,
            "tipoChamado":tipoChamado
        }
        chamados_previstos.append(chamado_previsto)
    return chamados_previstos