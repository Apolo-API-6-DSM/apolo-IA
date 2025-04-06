import pandas as pd
import joblib
import nltk
from PreProcessamento.preProcessar import pre_processar_treino
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from Metricas.metricas import gerar_metricas_emocoes
import os


base_dir = os.getcwd()

def treinarClassificacaoEmocao(df):
    # Pré-processamento
    df["Mensagem"] = [pre_processar_treino(texto) for texto in df["Mensagem"]]

    # Criando a bag_of_words com porcentagem de relevancia para cada palavra
    tfidf = TfidfVectorizer(ngram_range=(1, 2))
    tfidf_tratados = tfidf.fit_transform(df["Mensagem"])

    #Treinamento
    X_treino, X_teste, y_treino, y_teste = train_test_split(tfidf_tratados, df['Emocao'], test_size=0.2, random_state=42, stratify=df['Emocao'])
    regressao_logistica = LogisticRegression(class_weight='balanced')
    regressao_logistica.fit(X_treino, y_treino)
    gerar_metricas_emocoes(regressao_logistica, X_teste, y_teste)

    # Salvar o modelo e o vetorizador em arquivos
    joblib.dump(tfidf, f'{base_dir}\\Treinamento\\Exportados\\RegressaoLinear\\emocao_vetorizador_metricas.pkl')
    joblib.dump(regressao_logistica, f'{base_dir}\\Treinamento\\Exportados\\RegressaoLinear\\modelo_emocao_metricas.pkl')
    print("Modelo e vetorizador salvos com sucesso!")



if __name__ == "__main__":
    nltk.download('stopwords')
    nltk.download('rslp')
    dataset = f'{base_dir}\\Treinamento\\Datasets\\EmocoesDatasetTreinamento-v1.csv'
    
    # Carregar o dataset e verificar as classes
    df = pd.read_csv(dataset, sep=";", encoding="UTF-8", quotechar='"')
    classes_unicas = df['Emocao'].unique()
    print("\n\nClasses encontradas na coluna 'Emocao':")
    for i, classe in enumerate(classes_unicas):
        print(f"{i}: {classe}")

    # Conta as ocorrências de cada tipo
    contagem = df["Emocao"].value_counts()

    # Exibe o resultado
    print("\n\nDistribuição de exemplos por categoria:")
    print(contagem)
    treinarClassificacaoEmocao(df)