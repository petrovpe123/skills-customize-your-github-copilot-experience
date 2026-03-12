# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Build a small REST API with FastAPI and practice creating routes, handling request data, and returning JSON responses.

## 📝 Tasks

### 🛠️ Create Basic API Endpoints

#### Description
Use the provided `starter-code.py` file to create a FastAPI application with a few basic endpoints. Start by building routes that confirm the API is running and return a list of sample tasks.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Add a `GET /` route that returns a welcome message as JSON
- Add a `GET /tasks` route that returns a list of task items
- Return valid JSON responses from each route


### 🛠️ Add Create and Update Features

#### Description
Expand the API so users can add new tasks and update the completion status of an existing task. Store the task data in a Python list for this assignment.

#### Requirements
Completed program should:

- Add a `POST /tasks` route that accepts task data from the request body
- Assign a unique `id` to each new task
- Add a `PUT /tasks/{task_id}` route that updates the `completed` value for a task
- Return a clear error message when a task with the given `id` does not exist
- Test the API in the browser docs or with a tool such as Postman