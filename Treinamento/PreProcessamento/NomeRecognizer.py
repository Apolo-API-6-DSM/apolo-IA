from presidio_analyzer import RecognizerResult, EntityRecognizer

import spacy

# Carregar o modelo spaCy em português
nlp = spacy.load("pt_core_news_lg")

# Criar um reconhecedor personalizado para nomes usando spaCy
class NomeRecognizer(EntityRecognizer):  # Herdar de EntityRecognizer
    def __init__(self):
        supported_entities = ["PERSON"]  # Entidade que o reconhecedor detecta
        super().__init__(supported_entities=supported_entities, supported_language="pt")

    def load(self):  # Método obrigatório para reconhecedores personalizados
        pass

    def analyze(self, text, entities, nlp_artifacts=None):  # Método para análise de texto
        resultados = []
        doc = nlp(text)  # Processar o texto com spaCy

        # Iterar sobre as entidades detectadas pelo spaCy
        for ent in doc.ents:
            if ent.label_ == "PER":  # PER = Pessoa (nome)
                # Criar um objeto RecognizerResult para cada nome detectado
                resultado = RecognizerResult(
                    entity_type="NOME",
                    start=ent.start_char,
                    end=ent.end_char,
                    score=0.9  # Confiança da detecção
                )
                resultados.append(resultado)

        return resultados