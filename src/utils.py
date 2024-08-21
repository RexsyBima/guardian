from .models import NewsScraped
from src import cursor, conn, session, SQLAlchemyNewsItem
from sqlite3 import Cursor


def insert_to_db2(data: NewsScraped):
    data.authors = ", ".join(data.authors)
    data.tag_news = ", ".join(data.tag_news)
    item = SQLAlchemyNewsItem(**data.model_dump())  # flask sqlalchemy # django orm
    session.add(item)
    session.commit()
    return


def check_news_exist2(url: str):
    return bool(session.query(SQLAlchemyNewsItem).filter_by(url=url).first())


def insert_to_db(data: NewsScraped, cursor: Cursor = cursor):
    cursor.execute(
        """INSERT INTO news (title, tag_news, paragraphs, authors, published_time, url)VALUES (?,?,?,?,?,?)""",
        (
            data.title,
            ", ".join(data.tag_news),
            data.paragraphs,
            ", ".join(data.authors),
            data.published_time,
            data.url,
        ),
    )
    conn.commit()


def check_news_exist(url: str, cursor: Cursor = cursor):
    news = cursor.execute("""SELECT * FROM news WHERE url = ?""", (url,)).fetchone()
    if news:
        return True
    else:
        return False
