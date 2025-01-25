from flask import Flask

from app.logger import get_chess_logger, get_flask_handler


def create_app(chess_log_path):
    app = Flask(__name__)

    chess_logger = get_chess_logger(chess_log_path)

    return app
