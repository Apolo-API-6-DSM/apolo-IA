from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

def gerar_metricas_emocoes(modelotreinado, X_teste, y_teste):
     # Fazer previsões no conjunto de teste
    y_pred = modelotreinado.predict(X_teste)
    
    # Calcular métricas
    acuracia = accuracy_score(y_teste, y_pred)
    precisao = precision_score(y_teste, y_pred, average=None)  # Métricas por classe
    recall = recall_score(y_teste, y_pred, average=None)       # Métricas por classe
    f1 = f1_score(y_teste, y_pred, average=None)               # Métricas por classe
    matriz_confusao = confusion_matrix(y_teste, y_pred)
    
    # Exibir as métricas
    print(f"Acurácia: {acuracia:.4f}")
    print("\nMétricas por classe:")
    print(f"Precisão: {precisao}")
    print(f"Recall: {recall}")
    print(f"F1-score: {f1}")
    print("\nMatriz de Confusão:")
    print(matriz_confusao)
    
    # Exibir relatório de classificação
    print("\nRelatório de Classificação:")
    print(classification_report(y_teste, y_pred, target_names=["Positiva", "Neutra", "Negativa"]))


def gerar_metricas_tipo_chamados(modelotreinado, X_teste, y_teste):
     # Fazer previsões no conjunto de teste
    y_pred = modelotreinado.predict(X_teste)
    
    # Calcular métricas
    acuracia = accuracy_score(y_teste, y_pred)
    precisao = precision_score(y_teste, y_pred, average=None)  # Métricas por classe
    recall = recall_score(y_teste, y_pred, average=None)       # Métricas por classe
    f1 = f1_score(y_teste, y_pred, average=None)               # Métricas por classe
    matriz_confusao = confusion_matrix(y_teste, y_pred)
    
    # Exibir as métricas
    print(f"Acurácia: {acuracia:.4f}")
    print("\nMétricas por classe:")
    print(f"Precisão: {precisao}")
    print(f"Recall: {recall}")
    print(f"F1-score: {f1}")
    print("\nMatriz de Confusão:")
    print(matriz_confusao)
    
    # Exibir relatório de classificação
    print("\nRelatório de Classificação:")
    print(classification_report(y_teste, y_pred, target_names=["Reclamacao", "Pedido de Suporte", "Duvida"]))