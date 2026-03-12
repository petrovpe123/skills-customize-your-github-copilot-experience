# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API with FastAPI by creating endpoints, validating request data, and returning JSON responses.

## 📝 Tasks

### 🛠️	Create the FastAPI Application

#### Description
Set up a FastAPI project that can manage a small collection of books. Create the application object, define a data model for incoming book data, and add a home route that confirms the API is running.

#### Requirements
Completed program should:

- Create a FastAPI app instance named `app`
- Define a `Book` model with `title`, `author`, and `year` fields
- Add a `GET /` endpoint that returns a JSON welcome message
- Store book data in a Python list for this assignment


### 🛠️	Build and Test REST Endpoints

#### Description
Add endpoints that let users view all books, add a new book, and retrieve a single book by its index in the list. Test the API to confirm it returns the expected JSON responses.

#### Requirements
Completed program should:

- Add a `GET /books` endpoint that returns all books
- Add a `POST /books` endpoint that accepts book data and saves it
- Add a `GET /books/{book_id}` endpoint that returns one book or an error message if it does not exist
- Return JSON responses that clearly show the stored data
- Test at least one successful request for each endpoint

Example request body:

```json
{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "year": 2008
}
```

Example response from `GET /books`:

```json
[
  {
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "year": 2008
  }
]
```