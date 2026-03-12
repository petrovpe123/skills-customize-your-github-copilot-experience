from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class Book(BaseModel):
    title: str
    author: str
    year: int


books = []


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI books API."}


@app.get("/books")
def get_books():
    return books


@app.post("/books")
def create_book(book: Book):
    books.append(book.model_dump())
    return {"message": "Book added successfully.", "book": book.model_dump()}


@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id < 0 or book_id >= len(books):
        raise HTTPException(status_code=404, detail="Book not found")

    return books[book_id]