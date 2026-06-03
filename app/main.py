from fastapi import FastAPI

from app.routers.health import router as health_router # Importa a variável 'router' como health_router
from app.routers.foods import router as foods_router

app = FastAPI(
    title="NutriData AI",
    description="API para análise nutricional com Python, dados e IA.",
    version="0.1.0",
)

app.include_router(health_router) # Registra o grupo de rotas dentro da aplicação principal
app.include_router(foods_router)