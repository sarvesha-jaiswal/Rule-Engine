from flask import Flask
from app.database import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    with app.app_context():
        init_db()

    # Register the Blueprint
    from app.routes import rule_engine
    app.register_blueprint(rule_engine)

    return app
