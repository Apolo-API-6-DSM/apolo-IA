import pandas as pd
import joblib
import nltk
from PreProcessamento.preProcessar import pre_processar_treino
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from Metricas.metricas import gerar_metricas_tipo_chamados

def treinarClassificacaoTipoChamado(df):
    # Pré-processamento
    df["Mensagem"] = [pre_processar_treino(texto) for texto in df["Mensagem"]]

    # Criando a bag_of_words com porcentagem de relevancia para cada palavra
    tfidf = TfidfVectorizer(ngram_range=(1, 2))
    tfidf_tratados = tfidf.fit_transform(df["Mensagem"])

    #Treinamento
    X_treino, X_teste, y_treino, y_teste = train_test_split(tfidf_tratados, df['TipoChamado'], test_size=0.2, random_state=42, stratify=df['TipoChamado'])
    regressao_logistica = LogisticRegression(class_weight='balanced')
    regressao_logistica.fit(X_treino, y_treino)
    gerar_metricas_tipo_chamados(regressao_logistica, X_teste, y_teste)

    # Salvar o modelo e o vetorizador em arquivos
    joblib.dump(tfidf, 'Treinamento\\Exportados\\tipo_chamado_vetorizador_metricas.pkl')
    joblib.dump(regressao_logistica, 'Treinamento\\Exportados\\modelo_tipo_chamado_metricas.pkl')
    print("Modelo e vetorizador salvos com sucesso!")



if __name__ == "__main__":
    nltk.download('stopwords')
    nltk.download('rslp')
    dataset = "Treinamento\\Datasets\\TiposArquivosTreino-v1.csv"

    # Carregar o dataset e verificar as classes
    df = pd.read_csv(dataset)
    df = df[~df["TipoChamado"].isin(["Informacao", "Reincidencia"])].reset_index(drop=True)
    classes_unicas = df['TipoChamado'].unique()
    print("\n\nClasses encontradas na coluna 'TipoChamado':")
    for i, classe in enumerate(classes_unicas):
        print(f"{i}: {classe}")
    
    # Conta as ocorrências de cada tipo
    contagem = df["TipoChamado"].value_counts()

    # Exibe o resultado
    print("\n\nDistribuição de exemplos por categoria:")
    print(contagem)
    treinarClassificacaoTipoChamado(df)