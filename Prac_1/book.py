from fastapi import FastAPI
from fastapi import Body
from fastapi import HTTPException
from User_Inputs import Book
from typing import List

app=FastAPI()

BOOKS : List[Book] = []

"""BOOKS=[
    {"id":1,"title":"The Great Gatsby","author":"F. Scott Fitzgerald"},
    {"id":2,"title":"To Kill a Mockingbird","author":"Harper Lee"},
    {"id":3,"title":"1984","author":"George Orwell"},
    {"id":4,"title":"Kill me","author":"Ayush Lee"}
]"""

@app.get("/")             # defines the endpoint for the API, in this case the root endpoint.
async def root():
    return {"message":"Welcome to the book store API!"}   # returns a JSON response with a welcome message when the root endpoint is accessed.

@app.get("/books")           # defines the endpoint for the API, in this case the root endpoint.    #books is static path.
async def read_all_books():
    if BOOKS:
        return BOOKS
    else:
        raise HTTPException(status_code=404, detail="No books found")   # raises an HTTPException with a 404 status code and a custom error message if the BOOKS list is empty.

"""@app.get("/books/mybook")
async def read_my_book():
    return {"title":"The Great Gatsby","author":"F. Scott Fitzgerald"}"""

@app.get("/books/")     # book_id is a dynamic path parameter that can be used to retrieve specific book information.``
async def read_a_book_by_id(given_book_id : int):
    for book in BOOKS:
        if book.id == given_book_id:
            return book

    raise HTTPException(status_code=404, detail=f"Book {given_book_id} does not found")   # raises an HTTPException with a 404 status code and a custom error message if the book is not found.


"""@app.get("/books/")
async def read_a_Particular_book(given_book_id : int):
    books_to_return = []
    for book in BOOKS:
        if book.id == given_book_id:
            books_to_return.append(book)

    if not books_to_return:
        raise HTTPException(status_code=404, detail=f"Book {given_book_id} does not found")

    return books_to_return"""



@app.get("/books/author/{author}/")
async def read_a_book_by_author( author: str):
    filtered_books = []
    for book in BOOKS:
        if book.author.casefold() == author.casefold():
            filtered_books.append(book)
    
    if not filtered_books:
        raise HTTPException(status_code=404, detail=f"No books found by author {author}")

    return filtered_books

@app.get("/books/{given_book_id}/")
async def read_a_book_by_both(given_book_id: int, author: str):
    for book in BOOKS:
        if book.id == given_book_id and book.author.casefold() == author.casefold() :
            return book
    raise HTTPException(status_code=404, detail=f"Book {given_book_id} not found")

@app.post("/books/create_book")
async def create_book(new_book: List[Book]):
    BOOKS.extend(new_book)
    return f"User has entered:"


@app.put("/books/update_book")
async def update_book(updated_book: Book):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == updated_book.id:
            BOOKS[i] = updated_book
            return {"message": "Book updated successfully"}
    raise HTTPException(status_code=404, detail=f"Book {updated_book.id} not found")

@app.delete("/books/delete_book/{given_book_id}")
async def delete_book(given_book_id: int):
    for i, book in enumerate(BOOKS):
        if book.id == given_book_id:
            BOOKS.pop(i)
            break

"""@app.get("/books/author_wise/{author}")
async def read_books_by_author(author: str):
    books_by_author = []
    for book in BOOKS:
        if book.author.casefold() == author.casefold():
            books_by_author.append(book)

    if not books_by_author:
        raise HTTPException(status_code=404, detail=f"No books found by author {author}")

    return books_by_author"""


# input for post
"""[
{
    "id": "1",
    "title": "if we were villians",
    "author": "ayush yadav"
},
{
    "id": "2",
    "title": "Ravaan",
    "author": "amish tripathi"

},
{
    "id": "3",
    "title": "yes to a year",
    "author": "shonda rhimes"

},
{
    "id": "4",
    "title": "ram",
    "author": "amish tripathi"

},
{
    "id": "5",
    "title": "black hole theory",
    "author": "stephen hwakins"

},
{
    "id": "6",
    "title": "sita",
    "author": "amish tripathi"

}
]"""