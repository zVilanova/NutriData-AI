import requests

OPEN_FOOD_FACTS_SEARCH_URL = "https://world.openfoodfacts.org/cgi/search.pl"

HEADERS = {
    "User-Agent": "NutriDataAI/0.1.0 (guedesleonardo022@gmail.com)",
}

def search_products(query: str):
    response = requests.get(
        OPEN_FOOD_FACTS_SEARCH_URL,
        params={ # Dictionary de parâmetros que serão enviados na query string da URL
            "search_terms": query,
            "search_simple": 1,
            "action": "process",
            "json": 1,
            "page_size": 5,
        },
        headers=HEADERS,
        timeout=10,
    )

    response.raise_for_status() # Lança uma exceção se a API externa retornar erro HTTP
    return response.json() # Desserializa o body da response (JSON) em um dict/list em Python
