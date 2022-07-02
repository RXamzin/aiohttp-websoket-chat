from sqlalchemy.orm import declarative_base, sessionmaker, Session, Query
from sqlalchemy import Column, create_engine
from sqlalchemy import Integer, String
import typing

Base = declarative_base()
eng = create_engine('sqlite:///test.db', echo=True)
ses: Session = sessionmaker(bind=eng)()

class User(Base):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __new__(cls, *args, **kwargs):
        cls.query = Query(cls, ses)
        return super().__new__(cls)



u = User(username='s', password='g')
print(type(User))
User.query.all()