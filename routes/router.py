from fastapi import APIRouter
from controller.controller_Data import *
from model.dataModel import *

router = APIRouter()


@router.post("/insert_data")
async def insert_data(data : Data):
    return await create_Method(data)


@router.get("/get_Data")
async def get_existing_item(item: int):
    return await get_existing_items(item)


@router.post("/update_item/{key}")
async def update_existing_item(key: int, data: innerData):
    print(key, data)
    return await update_existing_items(key, data)


List_Of_Items = []
@router.delete("/delete_items/{key}")
async def delete_existing_items(key: int):
    return await delete_exisiting_items(key)