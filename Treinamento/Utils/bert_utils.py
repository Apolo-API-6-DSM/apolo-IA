# bert_utils.py

def get_tokenize_fn(tokenizer):
    def tokenize(example):
        return tokenizer(
            example["Mensagem"],
            padding="max_length",
            truncation=True,
            max_length=128
        )
    return tokenize
