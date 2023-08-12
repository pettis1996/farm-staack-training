from model import Todo

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client.TodoList
collection = database.todo

async def fetch_one_todo(title):
    document = await collection.find_one({"title":title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos