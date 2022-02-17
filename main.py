from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException

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

@app.post("/api/v1/users")
async def register(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code=404, 
        detail=f"user with id: {user_id} does not exist."
    )

#TODO: Run in terminal "uvicorn main:app --reload"
#52:13