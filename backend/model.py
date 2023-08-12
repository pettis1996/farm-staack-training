from pydantic import BaseModel, Field
from typing import Optional

class Todo(BaseModel):
    title: str
    description: str