from fastapi import APIRouter

# Cria um grupo de rotas começando com o prefixo /health, no grupo Health
router = APIRouter(
    prefix="/health",
    tags=["Health"],
)

@router.get("")
def health_check():
    return {
        "status" : "ok",
        "message" : "NutriData AI is running"
    }