from flask import request
from flask.views import MethodView
from db import tasks
from datetime import date, datetime
import uuid

class TaskListResources(MethodView):
    def get(self):
        completed = request.args.get("completed")

        if completed is not None:
            is_completed = completed.lower() == "true"

            filtered_tasks = {task_id : task for task_id , task in tasks.items() if task["completed"] == is_completed}
            return {"tasks" : list(filtered_tasks.values())} , 200

        return {"tasks" : list(tasks.values())} , 200
    
    def post(self):
        request_data = request.get_json()
        required_fields = ["name", "due_date"]
        for field in required_fields:
            if field not in request_data:
                return {"error": f"'{field}' is required."}, 400
        
        try:
            due_date = datetime.strptime(request_data["due_date"], "%d-%m-%Y").date()
        except ValueError:
            return {"error": "due_date must be in DD-MM-YYYY format."}, 400
        

        today = date.today().strftime("%d-%m-%Y")
        task_id = uuid.uuid4().hex
        task = {**request_data ,"due_date" : due_date.strftime("%d-%m-%Y"),"completed" : False, "created_at" : today ,"task_id": task_id}
        tasks[task_id] = task
        return tasks[task_id] , 201
    

class TaskResource(MethodView):
    def get(self ,task_id):
        try:
            return tasks[task_id] , 200
        except KeyError:
            return {"message" : "Task id not found"} , 404
        
    def put(self ,task_id):
        request_data = request.get_json()

        if task_id not in tasks:
            return {"message" : "Task id not found"} , 404
        
        allowed_fields = {"name", "description", "due_date", "completed"}
        
        for key in request_data:
            if key not in allowed_fields:
                return {"error": f"'{key}' is not an allowed field."}, 400
        
        if "due_date" in request_data:
            try:
                due_date = datetime.strptime(request_data["due_date"], "%d-%m-%Y").date()
                request_data["due_date"] = due_date.strftime("%d-%m-%Y")
            except ValueError:
                return {"error": "due_date must be in DD-MM-YYYY format."}, 400
            
        tasks[task_id].update(request_data)
        return tasks[task_id] , 200
    
    def delete(self ,task_id):
        try:
            del tasks[task_id]
            return {"message" : "Task deleted successfully"} , 200
        except KeyError:
            return {"message" : "Task id not found"} , 404