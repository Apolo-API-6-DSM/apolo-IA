from sklearn.metrics import classification_report
import numpy as np

def avaliar_modelo(trainer, ds_val):
    pred = trainer.predict(ds_val)
    y_true = pred.label_ids
    y_pred = np.argmax(pred.predictions, axis=1)
    return y_true, y_pred

def imprimir_relatorio(y_true, y_pred, id2label):
    nomes_classes = [id2label[i] for i in range(len(id2label))]
    print("\nRelatório de Classificação:")
    print(classification_report(y_true, y_pred, target_names=nomes_classes))