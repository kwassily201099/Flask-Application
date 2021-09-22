from flask import Flask, render_template
import os
from .models import db_session, init_db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
    init_db()

    # Make the storage directory.
    if not os.path.isdir("./conversation"):
        os.mkdir("./conversation")

    from .controllers import controllers
    app.register_blueprint(controllers)

    @app.teardown_request
    def shutdown_session(exception=None):
        db_session.remove()

    return app