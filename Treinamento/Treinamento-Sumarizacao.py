import evaluate
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq
from transformers import Seq2SeqTrainer, Seq2SeqTrainingArguments, EarlyStoppingCallback
from datasets import Dataset
import torch
import numpy as np
from evaluate import load

# Configuração do modelo
model_name = "csebuetnlp/mT5_multilingual_XLSum"

# Carregar tokenizer e modelo
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Função de pré-processamento otimizada
def preprocess_function(examples):
    inputs = ["summarize in portuguese: " + str(doc) for doc in examples['Descrição Dataset']]  # Instrução mais clara
    targets = [str(doc) for doc in examples['Resumo']]
    
    model_inputs = tokenizer(
        inputs,
        max_length=512,
        truncation=True,
        padding="max_length"
    )
    
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(
            text_target=targets,
            max_length=256,
            truncation=True,
            padding="max_length"
        )
    
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

# Configuração das métricas ROUGE
rouge = load("rouge")

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    
    # Geração mais controlada
    gen_kwargs = {
        "max_length": 256,
        "min_length": 40,  # Aumentado para resumos mais substantivos
        "num_beams": 4,
        "early_stopping": True,
        "no_repeat_ngram_size": 2,
        "temperature": 0.7,  # Adicionado para diversidade
        "top_k": 50,
        "top_p": 0.95
    }
    
    preds = predictions[0] if isinstance(predictions, tuple) else predictions
    preds = np.where(preds != -100, preds, tokenizer.pad_token_id)
    
    decoded_preds = tokenizer.batch_decode(
        model.generate(
            input_ids=torch.tensor(preds).to(model.device),
            **gen_kwargs
        ),
        skip_special_tokens=True
    )
    
    labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)
    
    # Filtro de qualidade
    decoded_preds = [p if len(p) > 20 else "Resumo não gerado adequadamente" for p in decoded_preds]
    
    result = rouge.compute(
        predictions=decoded_preds,
        references=decoded_labels,
        use_stemmer=True
    )
    
    # Exemplo detalhado
    print("\n=== Comparação ===")
    print(f"Original ({len(decoded_labels[0])} chars): {decoded_labels[0][:150]}...")
    print(f"Gerado ({len(decoded_preds[0])} chars): {decoded_preds[0][:150]}...")
    
    return {
        "rouge1": round(result["rouge1"], 4),
        "rouge2": round(result["rouge2"], 4),
        "rougeL": round(result["rougeL"], 4),
        "length_ratio": round(len(decoded_preds[0])/len(decoded_labels[0]), 2)
    }

def training():
    # Configurações de treinamento otimizadas para XLSum
    training_args = Seq2SeqTrainingArguments(
        output_dir='./results_xlsum_improved',
        eval_strategy="epoch",
        per_device_train_batch_size=4,  # Aumentado para melhor estabilidade
        per_device_eval_batch_size=4,
        learning_rate=3e-5,  # Ajuste fino do learning rate
        num_train_epochs=10,  # Mais épocas para convergência
        weight_decay=0.01,
        predict_with_generate=True,
        generation_max_length=256,
        generation_num_beams=4,
        save_strategy="epoch",
        logging_strategy="steps",
        logging_steps=100,
        load_best_model_at_end=True,
        metric_for_best_model="rougeL",
        greater_is_better=True,
        fp16=True if torch.cuda.is_available() else False,
        gradient_accumulation_steps=2,  # Reduzido para batch_size maior
        warmup_ratio=0.1,  # Melhor que steps absolutos
        report_to="none",
        label_smoothing_factor=0.1  # Adicionado para regularização
    )

    # Configurar data collator
    data_collator = DataCollatorForSeq2Seq(
        tokenizer,
        model=model,
        pad_to_multiple_of=8,
        label_pad_token_id=-100
    )

    # Inicializar o Trainer
    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_train,
        eval_dataset=tokenized_test,
        tokenizer=tokenizer,
        data_collator=data_collator,
        compute_metrics=compute_metrics,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=2)]
    )

    # Teste de geração pré-treinamento
    print("\nTeste de geração antes do treino:")
    sample_input = "summarize: " + df.iloc[0]['Descrição Dataset']
    inputs = tokenizer(sample_input, return_tensors="pt", truncation=True, max_length=512)
    outputs = model.generate(**inputs, max_length=256)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))

    # Iniciar treinamento
    trainer.train()
    
    # Salvar modelo e tokenizer
    model.save_pretrained("./Treinamento/Exportados/Sumarizacao")
    tokenizer.save_pretrained("./Treinamento/Exportados/Sumarizacao")

if __name__ == "__main__":
    # Carregar e preparar dados
    dataset_path = "./Treinamento/Datasets/corpus_fine_tunning.csv"
    df = pd.read_csv(dataset_path, sep=";", encoding="UTF-8", quotechar='"')
    
    # Limpeza de dados
    df = df.dropna(subset=['Descrição Dataset', 'Resumo'])
    df = df.applymap(str)  # Garantir que todos os dados são strings
    
    # Converter para Dataset
    dataset = Dataset.from_pandas(df)
    train_test_split = dataset.train_test_split(test_size=0.2)
    
    # Tokenização
    tokenized_train = train_test_split['train'].map(
        preprocess_function,
        batched=True,
        batch_size=8,
        remove_columns=dataset.column_names
    )
    tokenized_test = train_test_split['test'].map(
        preprocess_function,
        batched=True,
        batch_size=8,
        remove_columns=dataset.column_names
    )
    
    # Iniciar treinamento
    training()