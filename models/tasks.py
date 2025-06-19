from db import db

class TaskModel(db.Model):
    __tablename__ = "tasks"
    task_id = db.Column(db.Integer , primary_key=True,autoincrement=True)
    name = db.Column(db.String,nullable=False)
    due_date = db.Column(db.String,nullable=False)
    description = db.Column(db.String)
    completed = db.Column(db.Boolean,nullable=False,default=False)
    created_at = db.Column(db.String,nullable=False)