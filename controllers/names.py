import fastapi
from fastapi import Depends

import conf

from controllers.users import manager
from controllers.models import User

router = fastapi.APIRouter(prefix="/api/subscriptions", tags=['Subscriptions'])

# TODO: need add tests


@router.get('')
async def get_all_subscriptions():
    return {"subscriptions names": conf.FLOWS}


@router.get('/my')
async def get_my_subscriptions(_=Depends(manager)):
    return {'my_subscriptions': _.flow_subscriptions}


@router.post('/my')
async def update_my_subscriptions(subscriptions: str, _=Depends(manager)):
    _my_subscriptions = subscriptions.split(',')
    user = User.objects(name=_.name).first()
    user.update(flow_subscriptions=_my_subscriptions)
    return {'my_new_subscriptions': _my_subscriptions}
