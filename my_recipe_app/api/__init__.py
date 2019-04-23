from flask_restful import Api

from app import flaskAppInstace
from .task import Task
from .taskById import TaskById


restServer = Api(flaskAppInstace)

restServer.add_resource(Task, "/api/v1/task")
restServer.add_resource(TaskById, "/api/v1/task/id/<string:taskId>")