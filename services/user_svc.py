import datetime
from sqlalchemy import insert
from commands.db import getSession
from models.user_dto import UserDto
from models.user import DbUser

async def RegisterUser(userInfo: UserDto) -> bool:
    async with getSession() as connection_db_user:
        try:
            db_user = DbUser(azure_ad_id=userInfo.azure_ad_id, tenant_id=userInfo.tenant_id, email=userInfo.email, full_name=userInfo.full_name, last_login_at=datetime.datetime.now(datetime.timezone.utc))
            connection_db_user.add(db_user)
            connection_db_user.commit()
        except Exception as error:
            print('Error while RegisterUser method', error)
    return False