from flask import render_template

import signal

from . import bp

@bp.route('/')
def index():
    return render_template("index.html")

@bp.route('/about')
def about():
    return render_template("misc/about.html")

@bp.route('/settings')
def settings():
    user_settings = {
        "color_theme": "dark",
        "piece_style": "companion",
        "board_theme": "white_and_grey",
        "show_notation_during_training": "false",
        "show_variation_name_during_training": "false",
        "show_annotation_glyphs_during_training": "false",
        "show_move_comments_during_training": "false",
        "mute": "true",
        "display_name": "Test User"
    }

    return render_template('misc/settings.html', userSettings=user_settings)

@bp.route('/shutdown')
def shutdown():
    signal.raise_signal(signal.SIGINT)  # Sending signal to run.py to que destruction of the thread, & de-initializing

    return render_template("misc/shutdown.html")
