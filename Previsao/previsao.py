from PreProcessamento.preProcessamento import pre_processar
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import os
from transformers import BertTokenizer, BertForSequenceClassification
import torch
from Previsao.sumarizacao import sumarizacao

base_dir = os.getcwd()


modeloTipoChamadoClassificacao = BertForSequenceClassification.from_pretrained("Treinamento/Exportados/BERTClassificacao/TipoChamado/modelo")
tokenizerTipoChamado = BertTokenizer.from_pretrained("Treinamento/Exportados/BERTClassificacao/TipoChamado/tokenizer")
label_encoder_TipoChamado = joblib.load("Treinamento/Exportados/BERTClassificacao/TipoChamado/label_encoder.pkl")

modeloEmocaoClassificacao = BertForSequenceClassification.from_pretrained("Treinamento/Exportados/BERTClassificacao/Emocoes/modelo")
tokenizerEmocao = BertTokenizer.from_pretrained("Treinamento/Exportados/BERTClassificacao/Emocoes/tokenizer")
label_encoder_Emocao = joblib.load("Treinamento/Exportados/BERTClassificacao/Emocoes/label_encoder.pkl")


def preverClassificacao(texto, tokenizer, modelo, labelEncoder):
    inputs = tokenizer(texto, return_tensors="pt", truncation=True, padding=True, max_length=512)

    with torch.no_grad():
        outputs = modelo(**inputs)

    logits = outputs.logits
    predicted_class_id = torch.argmax(logits, dim=-1).item()

    predicted_class = labelEncoder.inverse_transform([predicted_class_id])[0]
    return predicted_class


def preverListaChamados(chamados):
    chamados_previstos = []
    for chamado in chamados:
        emocao = preverClassificacao(chamado["descricao"], tokenizerEmocao, modeloEmocaoClassificacao, label_encoder_Emocao)
        tipoChamado = preverClassificacao(chamado["descricao"], tokenizerTipoChamado, modeloTipoChamadoClassificacao, label_encoder_TipoChamado)
        resumo = sumarizacao(chamado["descricao"])
        chamado_previsto = {
            "chamadoId":chamado["chamadoId"],
            "decricao":chamado["descricao"],
            "emocao":emocao,
            "tipoChamado":tipoChamado,
            "sumarizacao": resumo
        }
        chamados_previstos.append(chamado_previsto)
    return chamados_previstos


