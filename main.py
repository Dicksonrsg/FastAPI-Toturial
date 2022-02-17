from typing import List
from uuid import uuid4
from fastapi import FastAPI

from models import Gender, Role, User

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Peter",
        last_name="Parker",
        middle_name="Hero",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="Mary",
        last_name="Parker",
        middle_name="Jane",
        gender=Gender.female,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {"Hello": "earth"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

#TODO: Run in terminal "uvicorn main:app --reload"
#24:53