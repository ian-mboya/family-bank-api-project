from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'j#r_!4b5m9h(4yw-5vzv95=o#6ehdk&(bs7tr(mu*li7%k5hi2'

    from .views import views
    from .formhandle import formhandle




    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(formhandle, url_prefix='/')


    return app