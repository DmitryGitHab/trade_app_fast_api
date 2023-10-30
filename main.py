from datetime import datetime
from enum import Enum

import uvicorn
from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel, Field

app = FastAPI(
    title="Trading App"
)


fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
    {"id": 4, "role": "admin", "name": "Alex", "degree": [
        {"id": 1, "created_at": "2020-01-01T00:00:00", "type_degree": "newbie"}]},
]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
]

fake_users2 = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]

# @app.get("/")
# def hello():
#     return  "hello world"

class DegreeType(Enum):
    newbie = 'newbie'
    expert = 'expert'


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType

class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = []


@app.get("/users/{user_id}", response_model=List[User])
def ger_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]
    # return user_id


@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 1):
    return fake_trades[offset:][:limit]


@app.post("/users/{user_id}")
# def change_user_name(user_id: int, new_name: str):
def change_user_degree(user_id: int, new_degree: str):
    current_user = list(filter(lambda user: user.get('id') == user_id, fake_users2))[0]
    current_user["type_degree"] = new_degree
    # return {"msg": f"{current_user.name} - > {current_user.degree}"}
    return {"msg": f"{current_user['name']} - > {current_user['type_degree']}"}

class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=50)
    side: str
    price: float = Field(ge=0)
    amount: float


@app.post("/trades/")
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}





if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)