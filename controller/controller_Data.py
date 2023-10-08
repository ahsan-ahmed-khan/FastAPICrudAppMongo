from fastapi import HTTPException
from database.database import database
from model.dataModel import Data
from services.DataServices import *


async def create_Method(data):
    create_item_ = await create_item(data)
    if create_item_:
        return create_item_
    else:
        HTTPException(status_code=500, detail="Failed to Create Item!")


async def get_existing_items(item):
    existing_item = await get_item(item)
    if existing_item:
        return existing_item
    else:
        HTTPException(status_code=500, detail="Item Not Found!")


async def update_existing_items(key, value):
    update_items = await update_item(key, value)
    if update_items :
        return update_items
    else:
        HTTPException(status_code=500, detail="Itrem Doesnot exist to update!")


async def delete_exisiting_items(key):
    delete_items = await delete_item(key)
    if delete_items:
        return delete_items
    else:
        return HTTPException(status_code=404, detail="Data For Deletion Doesnot Exist")