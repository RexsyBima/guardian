import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS news (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    tag_news TEXT,
    paragraphs TEXT NOT NULL,
    authors TEXT,
    published_time TEXT,
    url TEXT NOT NULL)
"""
)


conn.commit()
# conn.close()

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///database2.db", echo=True)
Base = declarative_base()


class SQLAlchemyNewsItem(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    tag_news = Column(String)
    paragraphs = Column(String, nullable=False)
    authors = Column(String)
    published_time = Column(String)
    url = Column(String)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
