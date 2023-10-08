from pydantic import BaseModel


class innerData(BaseModel):
    name: str
    age: int
    about: str


class Data(innerData):
    key: int
