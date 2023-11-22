import os
from apiflask import APIFlask

def create_app():
    app = APIFlask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        from . import endpoints

    return app