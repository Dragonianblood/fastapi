from fastapi import FastAPI
import uvicorn
import pygame as py

py.init()
app = FastAPI()
screen = py.Surface((0, 0))
clock = py.time.Clock()
running = True
dt = 0

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/about")
def read_about():
    return {"name": "Adriaan"}

@app.get("/users/{user_id}")
def read_user(user_id:str):
    return user_id


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
