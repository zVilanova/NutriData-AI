import requests
from fastapi import HTTPException

from app.clients.open_food_facts_client import search_products

def search_foods_by_query(query: str):
    query = query.strip()

    if not query:
        raise HTTPException(
            status_code=400,
            detail="Query parameter cannot be empty",
        )
    
    try:
        data = search_products(query) # Passa a query do usuário para a função da API externa

    except requests.Timeout:
        raise HTTPException(
            status_code=504,
            detail="Open Food Facts API timeout",
        )
    
    except requests.HTTPError:
        raise HTTPException(
            status_code=502,
            detail="Open Food Facts API returned an error",
        )
    
    except requests.RequestException:
        raise HTTPException(
            status_code=502,
            detail="Could not connect to Open Food Facts API",
        )
    
    products = data.get("products", []) # Pega a lista de produtos retornados pela API externa, caso não existam retorne uma lista vazia
    formatted_products = [] # Lista vazia para guardar os produtos formatados

    for product in products: # Percorre cada produto bruto retornado pela API externa
        nutriments = product.get("nutriments", {}) # Pega os nutrientes, caso não existam use um dictionary vazio

        formatted_products.append( # Adiciona um novo dictionary formatado na lista de produtos formatados
            {
                "name": product.get("product_name"),
                "brand": product.get("brands"),
                "categories": product.get("categories"),
                "calories_100g": nutriments.get("energy-kcal_100g"),
                "proteins_100g": nutriments.get("proteins_100g"),
                "carbohydrates_100g": nutriments.get("carbohydrates_100g"),
                "fat_100g": nutriments.get("fat_100g"),
                "sugars_100g": nutriments.get("sugars_100g"),
                "sodium_100g": nutriments.get("sodium_100g"),
                "nutriscore": product.get("nutriscore_grade"),
            }
        )
    
    return {
        "query": query,
        "total_results": data.get("count", 0), # Total de resultados encontrados pela Open Food Facts
        "results": formatted_products,
    }