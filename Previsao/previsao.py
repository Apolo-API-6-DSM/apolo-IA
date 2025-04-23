from PreProcessamento.preProcessamento import pre_processar
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import os
from transformers import BertTokenizer, BertForSequenceClassification
import torch

base_dir = os.getcwd()


modeloTipoChamadoTimbau = BertForSequenceClassification.from_pretrained("Treinamento/Exportados/BERTimbau/TipoChamado/modelo")
tokenizerTipoChamado = BertTokenizer.from_pretrained("Treinamento/Exportados/BERTimbau/TipoChamado/tokenizer")
label_encoder_TipoChamado = joblib.load("Treinamento/Exportados/BERTimbau/TipoChamado/label_encoder.pkl")

modeloEmocaoTimbau = BertForSequenceClassification.from_pretrained("Treinamento/Exportados/BERTimbau/Emocoes/modelo")
tokenizerEmocao = BertTokenizer.from_pretrained("Treinamento/Exportados/BERTimbau/Emocoes/tokenizer")
label_encoder_Emocao = joblib.load("Treinamento/Exportados/BERTimbau/Emocoes/label_encoder.pkl")


def preverTimbau(texto, tokenizer, modelo, labelEncoder):
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
        emocao = preverTimbau(chamado["descricao"], tokenizerEmocao, modeloEmocaoTimbau, label_encoder_Emocao)
        tipoChamado = preverTimbau(chamado["descricao"], tokenizerTipoChamado, modeloTipoChamadoTimbau, label_encoder_TipoChamado)
        #tipoDocumento = preverTipoDocumento(chamado["descricao"])
        chamado_previsto = {
            "chamadoId":chamado["chamadoId"],
            "decricao":chamado["descricao"],
            "emocao":emocao,
            "tipoChamado":tipoChamado
        }
        chamados_previstos.append(chamado_previsto)
    return chamados_previstos