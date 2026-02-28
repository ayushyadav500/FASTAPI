from fastapi import FastAPI
from User_Input_2 import Book
from typing import List

app=FastAPI()

BOOKS : List[Book] = []

@app.get("/")
async def read_root():
    return {"message": "Welcome to My Books API"}

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/books/create_book")
async def create_book(new_book: List[Book], embed: bool = True):
    BOOKS.extend(new_book)
    return f"User has entered: {new_book}"