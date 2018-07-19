# Author: Allen Anker
# Created by Allen Anker on 14/07/2018


from flask import Flask
from app.models.base import db
from flask_login import LoginManager


login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.settings')
    register_blueprint(app)

    db.init_app(app)
    login_manager.init_app(app)
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
