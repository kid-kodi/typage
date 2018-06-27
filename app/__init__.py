# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()

login = LoginManager()

def create_app(config_name):
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_object(app_config[config_name])
  app.config.from_pyfile('config.py')

  Bootstrap(app)
  db.init_app(app)

  login.init_app(app)
  login.login_message = "You must be logged in to access this page."
  login.login_view = "auth.login"

  migrate = Migrate(app, db)

  from app import models

  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)

  from .home import home as home_blueprint
  app.register_blueprint(home_blueprint)

  from .project import project as project_blueprint
  app.register_blueprint(project_blueprint)

  return app