import sys

from flask import Flask, render_template

from app.blueprints import main_blueprint
from app.logger import get_chess_logger

from threading import Thread


class App(Thread):
    def __init__(self, flask_app: Flask, chess_log_path: str):
        super().__init__()

        self.flask: Flask = flask_app

        # Flask Initialization
        self.flask.register_blueprint(main_blueprint)

        @self.flask.errorhandler(404)
        def page_not_found(e):
            return render_template("misc/404.html"), 404

        # Getting chess logging object
        self._chess_logger = get_chess_logger(chess_log_path)

    def run(self):
        self.flask.run()

    @staticmethod
    def exit():
        sys.exit(0)


def create_app(chess_log_path) -> App:
    app = App(Flask(__name__), chess_log_path)

    return app
