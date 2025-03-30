import re
from .anonimazer import anomalizer


def tornar_texto_legivel_humano(texto):
    texto = re.sub(r'\{.*?\}', ' ', texto)
    regex_caracteres_invalidos_link = r'[|\[\]<>]'
    texto_tratado = re.sub(regex_caracteres_invalidos_link, " ", texto)
    texto_tratado = anomalizer(texto_tratado)
    texto_tratado = re.sub(r'[ \t]+', ' ', texto_tratado)
    texto_tratado = re.sub(r'\n ', '\n', texto_tratado)
    texto_tratado = re.sub(r' \n', '\n', texto_tratado)
    texto_tratado = re.sub(r'\n\n+', '\n\n', texto_tratado)
    texto_tratado = re.sub(r'#gccode#\d+:\d+:\d+:[A-Za-z]+:\d+#', "", texto_tratado)
    return texto_tratado.strip()