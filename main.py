from fastapi import FastAPI
from fastapi.responses import HTMLResponse
#                          uv run fastapi dev main.py
posts = [
    {
        "id": 1,
        "title": "FastAPI Basics",
        "content": "Learning routes, request handling, and validation.",
        "published": True
    },
    {
        "id": 2,
        "title": "SQLAlchemy Intro",
        "content": "Understanding ORM and database sessions.",
        "published": False
    },
    {
        "id": 3,
        "title": "JWT Authentication",
        "content": "Securing APIs with tokens.",
        "published": True
    }
]

app = FastAPI()
@app.get("/", response_class = HTMLResponse,include_in_schema=False)
def home():
    return"<h1>You are home</h1>"
@app.get("/posts")
def get_posts():
    return posts