from flask import Flask , request
import uuid
from db import tasks

app = Flask(__name__)


@app.get("/tasks")
def get_tasks():
    return {"tasks" : list(tasks.values())} , 200

@app.get("/tasks/<string:task_id>")
def get_one_task(task_id):
    return tasks[task_id] , 200

@app.post("/tasks")
def create_tasks():
    request_data = request.get_json()
    task_id = uuid.uuid4().hex
    task = {**request_data , "task_id": task_id}
    tasks[task_id] = task
    return tasks[task_id] , 201

@app.delete("/tasks/<string:task_id>")
def delete_one_task(task_id):
    del tasks[task_id]
    return {"message" : "Task deleted successfully"} , 200