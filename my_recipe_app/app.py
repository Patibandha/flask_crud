from flask import Flask
import logging as logger
logger.basicConfig(level="DEBUG")






flaskAppInstace = Flask(__name__)


if __name__=='__main__':
    logger.debug("App Started")
    from api import *
    flaskAppInstace.run(debug=True, use_reloader=True)