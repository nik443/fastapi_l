from fastapi import FastAPI


app = FastAPI(
    title="Trading App"
)

fake_users = (
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "admin", "name": "Nikita"},
)


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]


fake_traders = [
    {
        "id": 1,
        "user_id": 1,
        "currency": "BTC",
        "side": "buy",
        "price": 123,
        "amount": 2.12,
    },
    {
        "id": 2,
        "user_id": 2,
        "currency": "BTC",
        "side": "buy",
        "price": 423,
        "amount": 4.12,
    },
    {
        "id": 3,
        "user_id": 3,
        "currency": "BTC",
        "side": "buy",
        "price": 423,
        "amount": 4.12,
    },
]


@app.get("/trades")
def get_trades(offset: int = 0, limit: int = 1):
    return fake_traders[offset:][:limit]


fake_users2 = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "admin", "name": "Nikita"},
]


@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    user = list(filter(lambda user: user.get("id") == user_id, fake_users2))[0]
    user["name"] = new_name
    return {"status": 200, "data": user}
