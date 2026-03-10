from fastapi import FastAPI, Body
from User_Input_2 import Book
from typing import List
from book_request import Book_Request


app=FastAPI()

BOOKS = []

@app.get("/")
async def read_root():
    return {"message": "Welcome to My Books API"}

@app.get("/books")
async def read_all_books():
    return BOOKS

"""@app.post("/books/create_book")
async def create_book(new_book: List[Book], embed: bool = True):
    BOOKS.extend(new_book)
    return f"User has entered: {new_book}"""

@app.post("/books/create_book")
async def create_book(create_book : Book_Request):
    BOOKS.append(create_book)
    return f"User has entered: {create_book}"

@app.delete("/books/delete_book/{book_id}")
async def delete_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            BOOKS.remove(book)
            return f"Book with id {book_id} has been deleted."
   # return f"Book with id {book_id} not found."