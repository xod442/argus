from flask import Flask
from flask_mongoengine import MongoEngine


db = MongoEngine()

def create_app(**config_overrides):
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    app.config.update(config_overrides)

    db.init_app(app)

    from main.views import main_app
    app.register_blueprint(main_app)

    from managers.views import managers_app
    app.register_blueprint(managers_app)

    from engineers.views import engineers_app
    app.register_blueprint(engineers_app)


    return app
