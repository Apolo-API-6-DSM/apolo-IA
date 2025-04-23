from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

def gerar_metricas_emocoes(modelotreinado, X_teste, y_teste):
     # Fazer previsões
    y_pred = modelotreinado.predict(X_teste)

    # Obter classes únicas e ordenar para consistência
    classes = sorted(y_teste.unique())
    
    # Calcular métricas
    acuracia = accuracy_score(y_teste, y_pred)
    precisao = precision_score(y_teste, y_pred, average=None, labels=classes)
    recall = recall_score(y_teste, y_pred, average=None, labels=classes)
    f1 = f1_score(y_teste, y_pred, average=None, labels=classes)
    matriz_confusao = confusion_matrix(y_teste, y_pred, labels=classes)

    # Exibir
    print(f"\nClasses encontradas na coluna 'Emocao':")
    for i, cls in enumerate(classes):
        print(f"{i}: {cls}")

    print(f"\nAcurácia: {acuracia:.4f}")
    print("\nMétricas por classe:")
    print(f"Precisão: {precisao}")
    print(f"Recall: {recall}")
    print(f"F1-score: {f1}")
    print("\nMatriz de Confusão:")
    print(matriz_confusao)

    print("\nRelatório de Classificação:")
    print(classification_report(y_teste, y_pred, labels=classes, target_names=classes))


def gerar_metricas_tipo_chamados(modelotreinado, X_teste, y_teste):
    y_pred = modelotreinado.predict(X_teste)

    classes = sorted(y_teste.unique())

    acuracia = accuracy_score(y_teste, y_pred)
    precisao = precision_score(y_teste, y_pred, average=None, labels=classes)
    recall = recall_score(y_teste, y_pred, average=None, labels=classes)
    f1 = f1_score(y_teste, y_pred, average=None, labels=classes)
    matriz_confusao = confusion_matrix(y_teste, y_pred, labels=classes)

    print(f"\nClasses encontradas na coluna do tipo de chamado:")
    for i, cls in enumerate(classes):
        print(f"{i}: {cls}")

    print(f"\nAcurácia: {acuracia:.4f}")
    print("\nMétricas por classe:")
    print(f"Precisão: {precisao}")
    print(f"Recall: {recall}")
    print(f"F1-score: {f1}")
    print("\nMatriz de Confusão:")
    print(matriz_confusao)

    print("\nRelatório de Classificação:")
    print(classification_report(y_teste, y_pred, labels=classes, target_names=classes))