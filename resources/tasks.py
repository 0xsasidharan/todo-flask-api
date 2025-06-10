from flask import request
from flask.views import MethodView
from flask_smorest  import Blueprint , abort 
from schemas import TaskSchema ,TaskUpdateSchema
from db import tasks
from datetime import date, datetime
import uuid

blp = Blueprint("tasks" , __name__ , description="Operations on tasks")


@blp.route("/tasks")
class TaskListResources(MethodView):
    @blp.response(200)
    def get(self):
        completed = request.args.get("completed")

        if completed is not None:
            if completed.lower() not in ["true", "false"]:
                return {"error": "Invalid value for 'completed'. Use 'true' or 'false'."}, 400
            is_completed = completed.lower() == "true"

            filtered_tasks = {task_id : task for task_id , task in tasks.items() if task["completed"] == is_completed}
            return {"tasks" : list(filtered_tasks.values())} , 200

        return {"tasks" : list(tasks.values())} , 200
    
    @blp.arguments(TaskSchema)
    @blp.response(201, TaskSchema)
    def post(self , request_data):

        try:
            due_date = datetime.strptime(request_data["due_date"], "%d-%m-%Y").date()
        except ValueError:
           abort (400, message="due_date must be in DD-MM-YYYY format.")
        

        today = date.today().strftime("%d-%m-%Y")
        task_id = uuid.uuid4().hex
        task = {**request_data ,"due_date" : due_date.strftime("%d-%m-%Y"),"created_at" : today ,"task_id": task_id}
        tasks[task_id] = task
        return tasks[task_id] , 201


@blp.route("/tasks/<string:task_id>")
class TaskResource(MethodView):
    @blp.response(200)
    def get(self ,task_id):
        try:
            return tasks[task_id] , 200
        except KeyError:
            abort (400, message="Task id not found")
    
    @blp.arguments(TaskUpdateSchema)
    @blp.response(200, TaskSchema)
    def put(self ,request_data, task_id):
        if task_id not in tasks:
            abort (400, message="Task id not found")
        
        if "due_date" in request_data:
            try:
                due_date = datetime.strptime(request_data["due_date"], "%d-%m-%Y").date()
                request_data["due_date"] = due_date.strftime("%d-%m-%Y")
            except ValueError:
                abort (400, message="due_date must be in DD-MM-YYYY format.")
            
        tasks[task_id].update(request_data)
        return tasks[task_id] , 200
    
    @blp.response(200)
    def delete(self ,task_id):
        try:
            del tasks[task_id]
            return {"message" : "Task deleted successfully"} , 200
        except KeyError:
            abort (400, message="Task id not found")