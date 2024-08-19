
#* Blueprints in Flask

from flask import Flask
from .main import main as main_blueprint


# Initialize Flask and Register the Blueprint
def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_blueprint)

    return app
