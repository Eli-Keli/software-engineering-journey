
#* Forms with WTForms

from flask import Flask
from .main import main as main_blueprint

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "myweaksecretkey"

    app.register_blueprint(main_blueprint)

    return app
