import os

from fastapi import FastAPI

server = FastAPI(openapi_prefix="/dev")


@server.get("/hello")
def hello():
    return {"message": "hello!"}


@server.get("/wassup")
def wassup():
    return {"message": "wassup?"}


@server.get("/bye")
def bye():
    return {"message": "bye!"}
