import fastapi
from fastapi import Depends, HTTPException, status
from starlette.responses import Response
from fastapi_login import LoginManager

from controllers.models import User

import conf

router = fastapi.APIRouter(prefix="/user", tags=['Users'])

manager = LoginManager(conf.SECRET_KEY, token_url='/user/login', use_cookie=True)


@manager.user_loader
def load_user(name: str):
    user = User.objects(name=name).first()
    return user


@router.post('/login')
def login(response: Response, user=Depends(load_user)):
    if user:
        token = manager.create_access_token(
            data=dict(sub=user.name)
            )
        manager.set_cookie(response, token)
        return response, {'success': True}
    return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect name",
            headers={"WWW-Authenticate": "Basic"},
        )


@router.post('/new')
async def add_new_user(name):
    user = User.objects(name=name)
    if user:
        return fastapi.HTTPException(
            status_code=400,
            detail="User with this email already exists.")
    new_user = User(name=name)
    new_user.save()
    response = {'Success': True}
    return fastapi.responses.JSONResponse(response)

