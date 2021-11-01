"""Run the API"""

from fastapi import APIRouter

from api.api_v1.endpoints import admins, login, predict, check_api


api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(check_api.router, prefix="/status", tags=["status"])
api_router.include_router(predict.router, prefix="/predict", tags=["predict"])
api_router.include_router(admins.router, prefix="/admins", tags=["admins"])
