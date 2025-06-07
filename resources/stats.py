from flask.views import MethodView
from db import tasks
from datetime import date, datetime




class StatsResource(MethodView):
    def get(self):
        completed_count = 0
        pending_count = 0
        overdue_count = 0

        for task in tasks.values():
            if task["completed"] == True:
                completed_count += 1
            else:
                pending_count += 1

        today = date.today()
        for task in tasks.values():
            due_date_str = task["due_date"]
            due_date = datetime.strptime(due_date_str, "%d-%m-%Y").date()
            if due_date < today and task["completed"] == False:
                overdue_count +=1
        
        return {
        "total_tasks" : len(tasks) ,
        "completed": completed_count,
        "pending": pending_count,
        "overdue": overdue_count
        }