from sqlalchemy import create_engine, Column, String, select, update, delete, insert, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
import databases
import uuid
import json

DATABASE_URL = "sqlite:///./articles.db"
database = databases.Database(DATABASE_URL)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Article(Base):
    __tablename__ = "articles"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    user_id = Column(String, index=True)

  


class ArticleManager:
    @classmethod
    def create_article(cls, db: Session, article_data: dict, user_id: str):
        article_data['id'] = str(uuid.uuid4())
        db_article = Article(**article_data, user_id=user_id)
        db.add(db_article)
        db.commit()
        db.refresh(db_article)
        return db_article
    
    @classmethod
    def fetch_user_articles(cls, db: Session, user_id: str):
        db_article = db.query(Article).filter(Article.user_id == user_id).all()
        return db_article
    
    @classmethod
    def get_all_articles(cls, db: Session):
        return db.query(Article).all()

    @classmethod
    def get_article(cls, db: Session, article_id: str):
        print("Fetching Article with id ",article_id )
        return db.query(Article).filter(Article.id == article_id).first()

    @classmethod
    def update_article(cls, db: Session, article_id: int, article_data: dict):
        db_article = db.query(Article).filter(Article.id == article_id).first()
        if db_article is None:
            return None
        for key, value in article_data.items():
            setattr(db_article, key, value)
        db.commit()
        db.refresh(db_article)
        return db_article

    @classmethod
    def delete_article(cls, db: Session, article_id: int):
        db_article = db.query(Article).filter(Article.id == article_id).first()
        if db_article is None:
            return None
        db.delete(db_article)
        db.commit()
        return {"message": "Article deleted successfully"}
    
Base.metadata.create_all(bind=engine)