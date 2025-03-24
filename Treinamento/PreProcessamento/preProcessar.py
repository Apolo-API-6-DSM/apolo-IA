import pandas as pd
from .eliminadorRuido import tornar_texto_legivel_humano
import re
import nltk
from nltk import tokenize
import unidecode
from nltk.stem import RSLPStemmer

stemmer = RSLPStemmer()

def pre_processar(texto):
    texto = tornar_texto_legivel_humano(texto)
    texto = re.sub(r'[^\w\s]', ' ', texto) #Tirar caracteres especiais
    texto = re.sub(r'\d+', ' ', texto)       # Remove números
    texto = re.sub(r'\b[^eé\s]\b', '', texto)#  Regex para identificar letras sozinhas que não sejam 'e' ou 'é'
    texto = texto.lower() #Deixar palavras em lowercase
    texto = unidecode.unidecode(texto) #Tirar acentuação
    #Tokenizar
    tokenizer = tokenize.WhitespaceTokenizer()
    texto = tokenizer.tokenize(texto)

    #Remoção de stopwords, aplicando stemming
    texto_tratado = []
    stop_words = nltk.corpus.stopwords.words('portuguese')
    for palavra in texto:
        if(palavra in stop_words):
            continue
        palavra = unidecode.unidecode(palavra) #Tirar acentuação
        palavra = stemmer.stem(palavra) #Aplicando o steamming
        texto_tratado.append(palavra)

    return ' '.join(texto_tratado)

    