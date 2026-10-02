# 🥗 NutriData AI - API de Análise Nutricional
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

Um projeto de estudo criado para consolidar conhecimentos em consumo de APIs externas com Python, desenvolvimento de Web APIs com FastAPI, manipulação de dados JSON e organização de responsabilidades em camadas.

## Visão Geral

NutriData AI é uma API construída em Python que consome dados públicos do Open Food Facts para buscar produtos alimentícios, normalizar informações nutricionais e retornar uma resposta simplificada e útil para análise.

O principal objetivo deste projeto é estudar, na prática, como as APIs funcionam em Python — desde o recebimento de uma requisição HTTP até o consumo de uma API externa e o tratamento da sua resposta.

Atualmente, o projeto inclui:

- Uma API REST construída com FastAPI
- Consumo da API pública do Open Food Facts
- Validação de parâmetros de entrada
- Tratamento de erros de integração externa
- Normalização de dados nutricionais
- Organização em camadas: routers, services e clients

## Objetivo de Aprendizado

Este projeto foi criado como parte do meu crescimento em Python, especialmente para entender melhor:

- Como criar endpoints com FastAPI
- Como consumir APIs externas com `requests`
- Como trabalhar com JSON em Python
- Como tratar erros HTTP
- Como separar responsabilidades em uma aplicação backend
- Como transformar dados brutos externos em respostas mais limpas e úteis

### Arquitetura

```mermaid
flowchart LR
    user["👤 Usuário<br/>Cliente HTTP"]
    api["🌐 FastAPI<br/>Aplicação principal"]
    router["🧭 Router<br/>foods.py"]
    service["🧠 Service<br/>food_service.py"]
    client["🔌 Client<br/>open_food_facts_client.py"]
    external["🥗 Open Food Facts<br/>API Externa"]

    user -->|"Requisição HTTP"| api
    api -->|"Encaminha a requisição"| router
    router -->|"Chama a função do service"| service
    service -->|"Solicita produtos"| client
    client -->|"GET /cgi/search.pl"| external

    external -.->|"JSON bruto"| client
    client -.->|"JSON desserializado"| service
    service -.->|"Dados formatados"| router
    router -.->|"Resposta final"| api
    api -.->|"Resposta HTTP"| user
```

Responsabilidades:

| Camada | Responsabilidade |
|---|---|
| `main.py` | Ponto de entrada da aplicação e registro dos routers |
| `routers/` | Define os endpoints da API |
| `services/` | Contém regras de negócio, validações e formatação dos dados |
| `clients/` | Isola a comunicação com APIs externas |

## Stack

| Camada | Tecnologia |
|---|---|
| Linguagem | Python |
| API | FastAPI |
| Servidor local | Uvicorn |
| Requisições HTTP | Requests |
| Fonte de dados | API do Open Food Facts |

## Endpoints da API

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/health` | Verifica se a API está em execução |
| `GET` | `/foods/search?query={value}` | Busca produtos no Open Food Facts e retorna dados nutricionais formatados |

## Exemplo de Requisição

```txt
GET /foods/search?query=banana
```

## Exemplo de Resposta

```json
{
  "query": "banana",
  "total_results": 11979,
  "results": [
    {
      "name": "Yogurt Bnine BANANA",
      "brand": "Jaouda",
      "categories": "Cow milk yogurts, Flavoured yogurts",
      "calories_100g": 88.1,
      "proteins_100g": 3.9,
      "carbohydrates_100g": 14.3,
      "fat_100g": 1.7,
      "sugars_100g": 9.3,
      "sodium_100g": 0,
      "nutriscore": "c"
    }
  ]
}
```

## Tratamento de Erros

A API trata alguns cenários importantes:

| Status | Situação |
|---|---|
| `400 Bad Request` | Query vazia ou contendo apenas espaços em branco |
| `502 Bad Gateway` | Erro retornado pela API externa |
| `504 Gateway Timeout` | Timeout ao consumir o Open Food Facts |

Exemplo:

```json
{
  "detail": "Query parameter cannot be empty"
}
```

## Executando Localmente

### Pré-requisitos

- Python 3.13+
- Git
- VS Code ou seu editor preferido

### Clone o repositório

```powershell
git clone https://github.com/zVilanova/NutriData-AI.git
cd NutriData-AI
```

### Crie um ambiente virtual

```powershell
python -m venv .venv
```

### Ative o ambiente virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

### Instale as dependências

```powershell
pip install -r requirements.txt
```

### Execute a aplicação

```powershell
uvicorn app.main:app --reload
```

A API estará disponível em:

```txt
http://127.0.0.1:8000
```

Documentação interativa:

```txt
http://127.0.0.1:8000/docs
```
