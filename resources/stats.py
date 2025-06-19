from flask.views import MethodView
from datetime import date, datetime
from flask_smorest  import Blueprint 
from models.tasks import TaskModel

blp = Blueprint("stats" , __name__ , description="Operations on stats")

@blp.route("/stats")
class StatsResource(MethodView):
    @blp.response(200)
    def get(self):
        completed_count = 0
        pending_count = 0
        overdue_count = 0
        today = date.today()
        tasks= TaskModel.query.all()
        for task in tasks:
            if task.completed == True:
                completed_count += 1
            else:
                pending_count += 1


                try:
                    due_date = datetime.strptime(task.due_date, "%d-%m-%Y").date()
                    if due_date < today:
                        overdue_count +=1
                except:
                    continue
        return {
        "total_tasks" : len(tasks) ,
        "completed": completed_count,
        "pending": pending_count,
        "overdue": overdue_count
        }