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