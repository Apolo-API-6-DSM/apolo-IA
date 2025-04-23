import pandas as pd
from PreProcessamento.eliminadorRuido import tornar_texto_legivel_humano
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import ConfusionMatrixDisplay, classification_report
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset, ClassLabel, Features, Value
from Utils.bert_utils import get_tokenize_fn
import transformers
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def treinarClassificacaoTipoChamado(df, le):

    features = Features({
        "Mensagem": Value("string"),
        "label": ClassLabel(num_classes=len(df["label"].unique()), names=[str(i) for i in sorted(df["label"].unique())])
    })

    dataset = Dataset.from_pandas(df[["Mensagem", "label"]], features=features)
    dataset = dataset.train_test_split(test_size=0.2, stratify_by_column="label", seed=24)

    # Tokenizer e modelo
    tokenizer = BertTokenizer.from_pretrained("neuralmind/bert-base-portuguese-cased")
    model = BertForSequenceClassification.from_pretrained("neuralmind/bert-base-portuguese-cased", num_labels=len(le.classes_))


    tokenized_dataset = dataset.map(get_tokenize_fn(tokenizer), batched=True)
    tokenized_dataset.set_format("torch", columns=["input_ids", "attention_mask", "label"])

    # Argumentos de treino
    training_args = TrainingArguments(
        output_dir="./Treinamento/Exportados/BERTimbau/TipoChamado",
        eval_strategy="epoch",
        save_strategy="epoch",
        logging_dir="./logs",
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=3,
        load_best_model_at_end=True,
        metric_for_best_model="accuracy",
        save_total_limit=2,
    )

        # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset["train"],
        eval_dataset=tokenized_dataset["test"],
        compute_metrics=compute_metrics,
    )

    # Treinar
    trainer.train()

    # Gerar e plotar a Confusion Matrix
    trainer.evaluate()

    # Salvar modelo e label encoder
    model.save_pretrained("Treinamento/Exportados/BERTimbau/TipoChamado/modelo")
    tokenizer.save_pretrained("Treinamento/Exportados/BERTimbau/TipoChamado/tokenizer")
    joblib.dump(le, "Treinamento/Exportados/BERTimbau/TipoChamado/label_encoder.pkl")



# Métricas
def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    preds = np.argmax(predictions, axis=1)

    # Relatório de classificação
    report = classification_report(labels, preds, target_names=le.classes_, output_dict=True)

    # Matriz de confusão
    cm = confusion_matrix(labels, preds)

    plt.figure(figsize=(10, 7))
    sns.heatmap(cm, annot=True, fmt='d', xticklabels=le.classes_, yticklabels=le.classes_, cmap='Blues')
    plt.xlabel('Predito')
    plt.ylabel('Real')
    plt.title('Matriz de Confusão')
    plt.tight_layout()
    plt.savefig("confusion_matrix.png")  # Ou plt.show() se quiser só exibir

    return {
        "accuracy": report["accuracy"],
        "macro_f1": report["macro avg"]["f1-score"],
        "macro_precision": report["macro avg"]["precision"],
        "macro_recall": report["macro avg"]["recall"],
    }



if __name__ == "__main__":
    dataset = "Treinamento\\Datasets\\TiposArquivosTreino-v1.csv"
    print(transformers.__version__)
    df = pd.read_csv(dataset)
    df = df[~df["TipoChamado"].isin(["Informacao", "Reincidencia"])].reset_index(drop=True)
    df["Mensagem"] = [tornar_texto_legivel_humano(texto) for texto in df["Mensagem"]]
    # Encode labels
    le = LabelEncoder()
    df["label"] = le.fit_transform(df["TipoChamado"])
    print(TrainingArguments)
    treinarClassificacaoTipoChamado(df, le)