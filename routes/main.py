from fastapi import APIRouter
from routes.user import user_router

main_route = APIRouter()

main_route.include_router(
  user_router
)