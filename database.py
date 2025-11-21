from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import Base

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/test_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Создает все таблицы в базе данных на основе моделей, 
    которые наследуются от Base
    """
    Base.metadata.create_all(bind=engine)

def get_db():
    """
    Генератор для получения сессии БД.
    Гарантирует закрытие сессии после использования.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

