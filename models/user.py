from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import DateTime, String, Uuid
from sqlalchemy.schema import FetchedValue
from sqlalchemy import MetaData, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class DbUser(Base):
    __tablename__ = 'users'
    __table_args__ = (UniqueConstraint('azure_ad_id', 'tenant_id'),)
    user_id = Column(Uuid, primary_key=True, server_default=FetchedValue())
    azure_ad_id = Column(String(255), nullable=False)
    tenant_id = Column(String(255), nullable=False)
    email = Column(String(255))
    full_name = Column(String(255))
    created_at = Column(DateTime(True), server_default=FetchedValue())
    last_login_at = Column(DateTime(True))