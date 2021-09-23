from fastapi import FastAPI
from routes.main import main_route

app = FastAPI()

#Controllers or routes
app.include_router(main_route)

