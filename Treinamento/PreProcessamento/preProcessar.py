import pandas as pd
from .eliminadorRuido import tornar_texto_legivel_humano
import re
import nltk
from nltk import tokenize
import unidecode
from nltk.stem import RSLPStemmer

stemmer = RSLPStemmer()

def pre_processar_treino(texto):
    texto = tornar_texto_legivel_humano(texto)
    texto = re.sub(r'[^\w\s]', ' ', texto) #Tirar caracteres especiais
    texto = re.sub(r'\d+', ' ', texto)       # Remove números
    texto = re.sub(r'\b[^eé\s]\b', '', texto) #  Regex para identificar letras sozinhas que não sejam 'e' ou 'é'
    texto = texto.lower() #Deixar palavras em lowercase

    #Tokenizar
    tokenizer = tokenize.WhitespaceTokenizer()
    texto = tokenizer.tokenize(texto)

    #Remoção de stopwords, aplicando stemming
    texto_tratado = []
    palavras_para_manter = {'não', 'mas', 'nunca', 'jamais', 'nem', 'ainda', 'já', 'só', 'que'}
    stop_words = set(nltk.corpus.stopwords.words('portuguese')) - palavras_para_manter
    for palavra in texto:
        if(palavra in stop_words):
            continue
        palavra = stemmer.stem(palavra) #Aplicando o steamming
        texto_tratado.append(palavra)

    return ' '.join(texto_tratado)
