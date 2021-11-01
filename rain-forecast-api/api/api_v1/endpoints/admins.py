"""The admin API route"""

from fastapi import APIRouter
from fastapi.params import Depends

from schemas import user_schema
from api import deps


router = APIRouter()

@router.post("/", name="Add a new model",)
async def add_model(current_user: user_schema.User = Depends(deps.get_current_admin_user)):
    """Add a new model.
    """
    return 201
