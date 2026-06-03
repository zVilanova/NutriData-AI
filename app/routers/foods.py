from fastapi import APIRouter
from app.services.food_service import search_foods_by_query

router = APIRouter(
    prefix="/foods", # Define a rota base deste router como "/foods"
    tags=["Foods"], # Organiza a documentação no /docs em um grupo chamado "Foods"
)


@router.get("/search")  # Decorator, registra a função "search_food" como uma rota GET /foods/search
def search_foods(query: str):
    return search_foods_by_query(query)