from flask_restful import Resource
import logging as logger


class TaskById(Resource):

    def get(self, taskId):
        logger.debug("get method of TaskById started ")
        return {"message" : "inside get method taskid={}".format(taskId)}, 200
        pass

    def post(self, taskId):
        logger.debug("post method of TaskById started")
        return {"message" : "inside post method taskid={}".format(taskId)}, 200
        pass

    def put(self, taskId):
        logger.debug("put method of TaskById started")
        return {"message" : "inside put method taskid={}".format(taskId)}, 200
        pass

    def delete(self, taskId):
        logger.debug("delete method of TaskById started")
        return {"message" : "inside delete method taskid={}".format(taskId)}, 200
        pass
