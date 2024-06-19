import os

from fastapi import FastAPI

server = FastAPI(openapi_prefix="/dev")


@server.get("/hello")
def hello():
    return {"message": "hello!"}
