# 🧠 apolo-IA - Sistema de Classificação de Chamados

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange)
![NLP](https://img.shields.io/badge/NLP-Processing-green)

Sistema de IA para classificação automática de:
- **Tipo de chamado** (reclamação, suporte, solicitação)
- **Sentimento** (positivo, neutro, negativo)

## 🚀 Começando Rápido

git clone https://github.com/seu-usuario/apolo-IA.git

cd apolo-IA

**Opção 1: Sem ambiente virtual (mais simples)**
    ```bash
    # Instale as dependências globalmente
    pip install -r requirements.txt

    # Execute o script principal
    python main.py

**Opção 2: Com ambiente virtual (recomendado)**
    ```bash
    # Crie o ambiente virtual
    python -m venv venv

    # Ative o ambiente
    # Linux/MacOS:
    source venv/bin/activate
    # Windows:
    .\venv\Scripts\activate

    # Instale as dependências
    pip install -r requirements.txt

    # Execute o script
    python main.py

    # Para desativar o ambiente depois
    deactivate

# Instale dependências
pip install -r requirements.txt

# Configure o ambiente (opcional)
cp .env.example .env

Arquivo .env
MONGO_URI="mongodb://usuario:senha@localhost:27017"  # Conexão com MongoDB

MONGODB_DBNAME="apolo_ia_db"                         # Nome do banco de dados

API_PORT=8080

# Baixe os modelos:

## Modelos de classificacao

[Link para os modelos](https://drive.google.com/drive/folders/1slgVvrHyo6IMvCJV4uIf3kxX-dL4q9Hp?usp=drive_link)

Extraia o zip na pasta Exportados com o nome BERTClassificacao

## Modelo de sumarizacao

[Link para modelo](https://drive.google.com/file/d/1YBfJtl_qVJk7WlAxkaoqOy-cWbJG-kVj/view?usp=sharing)

Extraia o zip na pasta Exportados com o nome Sumarizacao


# Execute a aplicação
python app.py

📂 Estrutura do Projeto
```text
apolo-IA/
├── PreProcessamento/      # Scripts de preparação de dados
├── Previsao/             # Modelos de inferência
├── Treinamento/          # Scripts para treinar modelos
├── shared/               # Utilitários compartilhados
├── venv/                 # Ambiente virtual (opcional)
├── .env                  # Configurações de ambiente
├── app.py                # Aplicação principal
├── chamados_porto.csv    # Dataset de exemplo
├── Jira Exportar CSV     # Exemplo de dados de entrada
├── requirements.txt      # Dependências principais
└── req/                  # Requisitos adicionais

🛠️ Funcionalidades
Classificação de Tipos:

Reclamação

Pedido de Suporte

Solicitação Geral

Incidente

Análise de Sentimento:

😊 Positivo

😐 Neutro

😠 Negativo

💾 Fontes de Dados
CSV (como chamados_porto.csv)

MongoDB (quando configurado)

API REST

Esses dados serão salvos no banco de dados do postgreSQL
