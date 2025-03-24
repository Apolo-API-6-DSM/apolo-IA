from PreProcessamento.preProcessamento import pre_processar
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

tfidf = joblib.load('Treinamento\\Exportados\\emocao_vetorizador.pkl')
modelo = joblib.load('Treinamento\\Exportados\\modelo_emocao.pkl')

def preverEmocao(texto):
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
        emocao = preverEmocao(chamado["descricao"])
        #tipoDocumento = preverTipoDocumento(chamado["descricao"])
        chamado_previsto = {
            "chamadoId":chamado["chamadoId"],
            "decricao":chamado["descricao"],
            "emocao":emocao,
            #"tipoDocumento":tipoDocumento
        }
        chamados_previstos.append(chamado_previsto)
    return chamados_previstos