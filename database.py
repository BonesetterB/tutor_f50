from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


db = create_engine("sqlite:///relaxs.db", echo=True)
Session = sessionmaker(bind=db)
session = Session()
