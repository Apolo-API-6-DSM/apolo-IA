import pandas as pd
from PreProcessamento.eliminadorRuido import tornar_texto_legivel_humano







if __name__ == "__main__":
    dataset = "Treinamento\\Datasets\\TiposArquivosTreino-v1.csv"
    df = pd.read_csv(dataset)
    df = df[~df["TipoChamado"].isin(["Informacao", "Reincidencia"])].reset_index(drop=True)
    df["Mensagem"] = [tornar_texto_legivel_humano(texto) for texto in df["Mensagem"]]