from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from config import config
import logging
from datetime import datetime

db = SQLAlchemy()
file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.INFO)
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)       
       
    app.logger.addHandler(file_handler)
    #Blueprint registration
    from .api import api as api_bp
    app.register_blueprint(api_bp,url_prefix='/api/v1')
    from .api import api_login as api_login_bp
    app.register_blueprint(api_login_bp,url_prefix='/api/v1/authentication')


    return app