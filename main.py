from fastapi import FastAPI
from db import engine, Base

from routes import authors, categories, posts, tags


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(authors.router)
app.include_router(categories.router)
app.include_router(posts.router)
app.include_router(tags.router)