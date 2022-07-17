from sqlalchemy import Column, create_engine, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

host = '127.0.0.1'
port = '3306'
data = 'op'
user = 'root'
password = '123456789'

DB_URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{data}?charset=utf8mb4'
engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()


class Article(Base):
	__tablename__ = 'article'
	id = Column(Integer, primary_key=True, autoincrement=True)
	title = Column(String(100))
	content = Column(Text)


Base.metadata.create_all()

