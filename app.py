from flask import Flask 
from resources.tasks import TaskListResources , TaskResource
from resources.stats import StatsResource
app = Flask(__name__)

app.add_url_rule("/tasks", view_func=TaskListResources.as_view("task_list"))
app.add_url_rule("/tasks/<string:task_id>", view_func=TaskResource.as_view("task_detail"))
app.add_url_rule("/stats", view_func=StatsResource.as_view("stats"))
