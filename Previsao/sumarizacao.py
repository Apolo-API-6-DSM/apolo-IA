import os
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_path = os.path.abspath("./Treinamento/Exportados/Sumarizacao/model")

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model directory not found at: {model_path}")

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

# GPU, se disponível
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
model.eval()

# (Opcional, se estiver usando PyTorch 2.0+)
model = torch.compile(model)

def sumarizacao(text):
    text = "summarize in portuguese: " + text
    text = text.replace("<", "").replace(">", "")
    inputs = tokenizer.encode(text, max_length=512, truncation=True, return_tensors='pt').to(device)
    with torch.inference_mode():
        summary_ids = model.generate(
            inputs,
            max_length=74,
            min_length=32,
            num_beams=3,  # menor = mais rápido
            no_repeat_ngram_size=3,
            early_stopping=True
        )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return ' '.join(summary.split()).strip()
