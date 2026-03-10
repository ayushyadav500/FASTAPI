from pydantic import BaseModel

class Book_Request(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int

