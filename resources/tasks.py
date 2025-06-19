from flask import request
from flask.views import MethodView
from flask_smorest  import Blueprint , abort 
from schemas import TaskSchema ,TaskUpdateSchema
from datetime import date, datetime
from db import db
from models.tasks import TaskModel

blp = Blueprint("tasks" , __name__ , description="Operations on tasks")


@blp.route("/tasks")
class TaskListResources(MethodView):
    @blp.response(200, TaskSchema(many=True))
    def get(self):
        completed = request.args.get("completed")

        if completed is not None:
            if completed.lower() not in ["true", "false"]:
                abort(400 , message="Invalid value for 'completed'. Use 'true' or 'false'.")
            is_completed = completed.lower() == "true"
       
            return TaskModel.query.filter_by(completed=is_completed).all()

        return TaskModel.query.all() , 200
    
    @blp.arguments(TaskSchema)
    @blp.response(201, TaskSchema)
    def post(self , request_data):

        try:
            due_date = datetime.strptime(request_data["due_date"], "%d-%m-%Y").date()
        except ValueError:
           abort (400, message="due_date must be in DD-MM-YYYY format.")
        

        today = date.today().strftime("%d-%m-%Y")
        new_task = TaskModel(name=request_data.get("name") ,description=request_data.get("description"), due_date =due_date.strftime("%d-%m-%Y"),created_at=today,completed= request_data.get("completed", False))
        db.session.add(new_task)

        try:
            db.session.commit()
        except:
            db.session.rollback()
            abort(500 , message="Database error while creating task")
        return new_task


@blp.route("/tasks/<string:task_id>")
class TaskResource(MethodView):
    @blp.response(200 , TaskSchema)
    def get(self ,task_id):
        task = TaskModel.query.get(task_id)
        if task is None:
            abort(404 , message="Task Id not found")
        return task
    
    @blp.arguments(TaskUpdateSchema)
    @blp.response(200, TaskSchema)
    def put(self ,request_data, task_id):
        task= TaskModel.query.get(task_id)

        if task is None:
            abort (400, message="Task id not found")
        if "name" in request_data:
            task.name = request_data["name"]

        if "description" in request_data:
            task.description = request_data["description"]

        if "completed" in request_data:
            task.completed = request_data["completed"]
        
        if "due_date" in request_data:
            try:
                due_date = datetime.strptime(request_data["due_date"], "%d-%m-%Y").date()
                task.due_date = due_date.strftime("%d-%m-%Y")
            except ValueError:
                abort (400, message="due_date must be in DD-MM-YYYY format.")


        try:
            db.session.commit()
        except:
            db.session.rollback()
            abort(500 , message="Database error while deleting user")
        return task
    
    @blp.response(200)
    def delete(self ,task_id):
        
        task = TaskModel.query.get(task_id)

        if task is None:
            abort (404, message="Task id not found")

        db.session.delete(task)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            abort(500, message="Database error while deleting task")

        return {"message" : "Task deleted successfully"} , 200
        