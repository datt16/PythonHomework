from flask import Flask, make_response, jsonify
from .views.task import task_router
from flask_cors import CORS
from api.database import db
import config

def create_app():
    app = Flask(__name__, static_folder='../dist/static', template_folder='../dist')
    app.config.from_object('config.Config')
    db.init_app(app)

    app.register_blueprint(task_router, url_prefix='/api')
    CORS(app)
    return app

app = create_app()
