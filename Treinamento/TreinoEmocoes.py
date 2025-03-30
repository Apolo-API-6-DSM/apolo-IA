import pandas as pd
import joblib
import nltk
from PreProcessamento.preProcessar import pre_processar_treino
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from Metricas.metricas import gerar_metricas_emocoes

def treinarClassificacaoEmocao(dataset):
    # Pré-processamento
    df = pd.read_csv(dataset, sep=";", encoding="UTF-8", quotechar='"')
    df["Mensagem"] = [pre_processar_treino(texto) for texto in df["Mensagem"]]

    # Criando a bag_of_words com porcentagem de relevancia para cada palavra
    tfidf = TfidfVectorizer()
    tfidf_tratados = tfidf.fit_transform(df["Mensagem"])

    #Treinamento
    X_treino, X_teste, y_treino, y_teste = train_test_split(tfidf_tratados, df['Emocao'])
    regressao_logistica = LogisticRegression()
    regressao_logistica.fit(X_treino, y_treino)
    gerar_metricas_emocoes(regressao_logistica, X_teste, y_teste)

    # Salvar o modelo e o vetorizador em arquivos
    joblib.dump(tfidf, 'Treinamento\\Exportados\\emocao_vetorizador.pkl')
    joblib.dump(regressao_logistica, 'Treinamento\\Exportados\\modelo_emocao.pkl')
    print("Modelo e vetorizador salvos com sucesso!")



if __name__ == "__main__":
    nltk.download('stopwords')
    nltk.download('rslp')
    dataset = "Treinamento\\Datasets\\EmocoesDatasetTreinamento-v1.csv"
    treinarClassificacaoEmocao(dataset)