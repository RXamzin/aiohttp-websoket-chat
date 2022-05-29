from app.tools.db import Base

from sqlalchemy import Column
from sqlalchemy import Integer, String


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
