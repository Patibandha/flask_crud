from flask_restful import Resource
import logging as logger


class Task(Resource):

    def get(self):
        logger.debug("get method started")
        return {"message" : "inside get method"}, 200
        pass

    def post(self):
        logger.debug("post method started")
        return {"message" : "inside post method"}, 200
        pass

    def put(self):
        logger.debug("put method started")
        return {"message" : "inside put method"}, 200
        pass

    def delete(self):
        logger.debug("delete method started")
        return {"message" : "inside delete method"}, 200
        pass
