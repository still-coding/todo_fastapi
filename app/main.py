from fastapi import FastAPI
from . import models
from .database import create_db_and_tables, engine
from sqlmodel import Session
app = FastAPI()



@app.on_event("startup")
def startup_event():
    create_db_and_tables()
    with Session(engine) as session:
        users = [
            models.User(
                name="user1", email="user1@example.com", password="password1"
            ),
            models.User(
                name="user2", email="user2@example.com", password="password2"
            ),
        ]
        for u in users:
            session.add(u)
        session.commit()
        



@app.get("/")
async def root():
    return {"message": "Hello World"}