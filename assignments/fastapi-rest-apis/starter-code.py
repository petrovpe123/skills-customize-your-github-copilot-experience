from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    completed: bool


tasks = [
    {"id": 1, "title": "Learn FastAPI basics", "completed": False},
    {"id": 2, "title": "Build a REST endpoint", "completed": True},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def create_task(task: TaskCreate):
    next_id = max((item["id"] for item in tasks), default=0) + 1
    new_task = {"id": next_id, "title": task.title, "completed": False}
    tasks.append(new_task)
    return new_task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = task_update.completed
            return task

    raise HTTPException(status_code=404, detail="Task not found")