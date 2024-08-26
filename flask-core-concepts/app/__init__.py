
#* SQLAlchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .main import main as main_blueprint

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "myweaksecretkey"

    # Setup the database URI
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'

    # Initialize SQLAlchemy
    db.init_app(app)


    app.register_blueprint(main_blueprint)

    return app
