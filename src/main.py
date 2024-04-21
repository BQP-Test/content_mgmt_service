from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .database import engine, Base, SessionLocal , Article, ArticleManager
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .utils import NotifierClient, UserProfileClient

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)


    # Add other fields as needed
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/articles/")
async def get_all_articles(db: Session = Depends(get_db)):
    db_article = ArticleManager.get_all_articles(db)
    return db_article

@app.post("/articles/")
async def create_article(article_data: dict, user_id: str, db: Session = Depends(get_db)):
    db_article = ArticleManager.create_article(db, article_data, user_id=user_id)
    profile = UserProfileClient(user_id).get_user_profile()
    NotifierClient(profile['followers'] , db_article.id)
    return db_article

@app.get("/articles/manage/{user_id}")
async def fetch_user_articles(user_id: str, db: Session = Depends(get_db)):
    db_article = ArticleManager.fetch_user_articles(db, user_id=user_id)
    return db_article

@app.get("/articles/{article_id}/")
async def read_article(article_id: str, db: Session = Depends(get_db)):
    db_article = ArticleManager.get_article(db, article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article

@app.put("/articles/{article_id}")
async def update_article(article_id: str, article_data: dict, db: Session = Depends(get_db)):
    db_article = ArticleManager.update_article(db, article_id, article_data)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article

@app.delete("/articles/{article_id}")
async def delete_article(article_id: str, db: Session = Depends(get_db)):
    deleted_article = ArticleManager.delete_article(db, article_id)
    if deleted_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return deleted_article
