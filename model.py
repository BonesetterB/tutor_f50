from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    Name = Column(String(50), unique=False, nullable=False)
    Sport = Column(String(50), unique=False, nullable=False)
    