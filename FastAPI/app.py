from fastapi import FastAPI

app=FastAPI()


@app.get("/")
def home():
    return "Home"


@app.put("/users:user_name")
def user(user_name:str | None):
    print(user_name,user_name)

