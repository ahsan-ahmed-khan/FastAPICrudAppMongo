from fastapi import FastAPI

from routes.node import Node

app = FastAPI()
app.include_router(Node)

