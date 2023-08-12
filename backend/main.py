from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  

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