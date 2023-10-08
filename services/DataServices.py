from fastapi import HTTPException
from pymongo import ReturnDocument

from database.database import database
from model.dataModel import *


async def create_item(data):
    await database.connect()
    collection = database.get_collection()

    # Assuming data.key is a dictionary key to check for existence
    find_one_result = await collection.find_one({"key": data.key})

    if find_one_result:
        return {"response": "Key Already Exists!"}

    result = await collection.insert_one(data.dict())

    if result.inserted_id:
        return data
    else:
        return None


# async

async def get_item(key: int):
    await database.connect()
    collections = database.get_collection()

    item = await collections.find_one({"key" : key})

    if item:
        return Data(**item)
    else:
        return None

async def update_item(key, data):
    await database.connect()
    collections = database.get_collection()

    item = await collections.find_one_and_update(
        {"key": key},
        {"$set": data.dict()},
        return_document=ReturnDocument.AFTER  # Return the updated document
    )
    if item.inserted_id:
        return {"data" : { "Response" : data}}
    else:
        return None


async def delete_item(key):
    await database.connect()
    collections = database.get_collection()

    item = await collections.find_one({"key": key})
    if item:
        delete_result = await collections.delete_one({"_id": item["_id"]})
        if delete_result.deleted_count > 0:
            return Data(**item)
        else:
            return None
    else:
        return None