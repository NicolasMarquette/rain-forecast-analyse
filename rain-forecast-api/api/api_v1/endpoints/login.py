"""Security and authorization management"""

from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from api import deps
from core import security
from schemas import token_schema


router = APIRouter()


@router.post("/login/access-token", response_model=token_schema.Token)
def login_for_access_token(
    db = Depends(deps.get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
):
    """Give a token for the authorization.
    \f
    Parameter
    ---------
    form_data : OAuth2PasswordRequestForm
        The authorization request form.
    
    Raise
    -----
    HTTPException : 401
        Incorrect username or password if the username or the password input is not correct.
    
    Return
    ------
    dict : A dictionnary with the token and the type of token.    
    """
    user = security.authenticate_user(
        db, username=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = security.create_access_token(
        data={"sub": user.username},
    )
    return {"access_token": access_token, "token_type": "bearer"}
