# 🥗 NutriData AI - API de Análise Nutricional 

Projeto de estudo para consolidar conhecimentos em consumo de APIs externas com Python, desenvolvimento de Web APIs com FastAPI, tratamento de dados em JSON e organização de responsabilidades em camadas.

## Visão Geral

NutriData AI é uma API desenvolvida em Python que consome dados públicos da Open Food Facts para buscar produtos alimentícios, normalizar informações nutricionais e retornar uma resposta simplificada e útil para análise.

O objetivo principal do projeto é estudar, na prática, como APIs funcionam em Python, desde o recebimento de uma requisição HTTP até o consumo de uma API externa e o tratamento da resposta.

Atualmente, o projeto conta com:

- API REST desenvolvida com FastAPI
- Consumo da API pública Open Food Facts
- Validação de parâmetros de entrada
- Tratamento de erros de integração externa
- Normalização de dados nutricionais
- Organização em camadas: routers, services e clients

## Objetivo de Aprendizado

Este projeto foi criado como parte da minha evolução em Python, especialmente para entender melhor:

- Como criar endpoints com FastAPI
- Como consumir APIs externas com `requests`
- Como trabalhar com JSON em Python
- Como tratar erros HTTP
- Como separar responsabilidades em uma aplicação backend
- Como transformar dados externos brutos em respostas mais limpas e úteis

### Arquitetura

```mermaid
flowchart LR
    user["👤 Usuário<br/>Cliente HTTP"]
    api["🌐 FastAPI<br/>Aplicação principal"]
    router["🧭 Router<br/>foods.py"]
    service["🧠 Service<br/>food_service.py"]
    client["🔌 Client<br/>open_food_facts_client.py"]
    external["🥗 Open Food Facts<br/>API externa"]

    user -->|"HTTP Request"| api
    api -->|"Direciona rota"| router
    router -->|"Chama função de serviço"| service
    service -->|"Solicita produtos"| client
    client -->|"GET /cgi/search.pl"| external

    external -.->|"JSON bruto"| client
    client -.->|"JSON desserializado"| service
    service -.->|"Dados formatados"| router
    router -.->|"Resposta final"| api
    api -.->|"HTTP Response"| user
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
| Fonte de dados | Open Food Facts API |

## Endpoints da API

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/health` | Verifica se a API está funcionando |
| `GET` | `/foods/search?query={valor}` | Busca produtos na Open Food Facts e retorna dados nutricionais formatados |

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
| `400 Bad Request` | Query vazia ou contendo apenas espaços |
| `502 Bad Gateway` | Erro retornado pela API externa |
| `504 Gateway Timeout` | Timeout ao tentar consumir a Open Food Facts |

Exemplo:

```json
{
  "detail": "Query parameter cannot be empty"
}
```

## Rodando Localmente

### Pré-requisitos

- Python 3.13+
- Git
- VS Code ou editor de preferência

### Clonar o repositório

```powershell
git clone https://github.com/zVilanova/NutriData-AI.git
cd NutriData-AI
```

### Criar ambiente virtual

```powershell
python -m venv .venv
```

### Ativar ambiente virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

### Instalar dependências

```powershell
pip install -r requirements.txt
```

### Executar aplicação

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

## Status do Projeto

Projeto em desenvolvimento.

A versão atual tem como foco o aprendizado dos fundamentos de APIs em Python, incluindo criação de endpoints, consumo de API externa, tratamento de JSON, validação de entrada e separação inicial de responsabilidades.

## Próximas Melhorias

- [ ] Criar schemas com Pydantic para padronizar os contratos da API
- [ ] Adicionar análise nutricional com pandas
- [ ] Criar endpoint `/foods/analyze`
- [ ] Integrar Gemini para geração de insights nutricionais
- [ ] Criar endpoint `/foods/insights`
- [ ] Mover configurações sensíveis para variáveis de ambiente
- [ ] Melhorar documentação dos exemplos de uso
