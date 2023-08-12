import motor.motor_asyncio
from bson import ObjectId
from database import fetch_all_todos, fetch_one_todo, create_todo, update_todo, remove_todo
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo

app = FastAPI(debug=True)

origins = [
    'https://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_all_todos():
    return {"message": "Hello World."}

@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_title(title: str):
    response = await fetch_one_todo(title)
    if response: 
        return response
    raise HTTPException(404, f"There is no todo item with title: [{title}].")

@app.post("/api/todo", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad Request.")

@app.put("/api/todo/{title}", response_model=Todo)
async def put_todo(title: str, descr: str):
    response = await update_todo(title, descr)
    if response:
        return True 
    raise HTTPException(404, f"There is no todo item with title: [{title}].")


@app.delete("/api/todo/{title}")
async def delete_todo_by_id(title: str):
    response = await remove_todo(title)
    if response:
        return f"Successfully deleted todo: [{title}]"