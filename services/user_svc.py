import datetime
from sqlalchemy.dialects.postgresql import insert
from commands.db import getSession
from models.user_dto import UserDto
from models.user import DbUser

async def RegisterUser(userInfo: UserDto) -> bool:
    async with getSession() as connection_db_user:
        try:
            #db_user = DbUser(azure_ad_id=userInfo.azure_ad_id, tenant_id=userInfo.tenant_id, email=userInfo.email, full_name=userInfo.full_name, last_login_at=datetime.datetime.now(datetime.timezone.utc))
            # connection_db_user.add(db_user)
            # connection_db_user.commit()

            # Create an update/insert statement for the "Users" table
            stmt = insert(DbUser).values(userInfo.to_dict(include_none=False)).returning(DbUser.user_id).on_conflict_do_update(
                index_elements=['azure_ad_id', 'tenant_id'],  # the unique constraint or index for conflict resolution
                set_={'last_login_at': datetime.datetime.now(datetime.timezone.utc)}  # Update specific fields on conflict
            )
            result = connection_db_user.execute(stmt)
            connection_db_user.commit()
            data = result.fetchone()
            return data[0]
        except Exception as error:
            print('Error while RegisterUser method', error)
    return False