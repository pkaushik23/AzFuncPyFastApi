from contextlib import asynccontextmanager, contextmanager
import os
import sys

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
this = sys.modules[__name__]
load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)
db_session = sessionmaker(bind=engine)

@asynccontextmanager
async def getSession():
    db = db_session()
    try:
        yield db
    finally:
        db.close()