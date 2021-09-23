from fastapi import FastAPI
from routes.main import main_route

app = FastAPI(
  # Agregar documentación general al swagger
  title="CRUD con Fastapi by @camilo0119",
  version="0.0.1",
  openapi_tags=[{
    "name": "users",
    "description": "Users endpoints"
  }]
)

#Controllers or routes
app.include_router(main_route)

