from flask import Flask, render_template

from app.blueprints import main_blueprint

from app.logger import get_chess_logger


def create_app(chess_log_path):
    app = Flask(__name__)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("misc/404.html"), 404

    app.register_blueprint(main_blueprint)

    chess_logger = get_chess_logger(chess_log_path)

    return app
