import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Caminho absoluto para evitar problemas
model_path = os.path.abspath("./Treinamento/Exportados/Sumarizacao/model")

# Verificar se o caminho existe
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model directory not found at: {model_path}")

# Carregar tokenizer e modelo
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)  # Removi from_flax=True a menos que seja necessário

def sumarizacao(text):
    text = text.replace("<", "").replace(">", "")
    inputs = tokenizer.encode(text, max_length=512, truncation=True, return_tensors='pt')
    summary_ids = model.generate(inputs, max_length=74, min_length=32, num_beams=5, no_repeat_ngram_size=3, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0])
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    summary = ' '.join(summary.split()).strip()
    return summary
