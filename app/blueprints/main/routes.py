from flask import render_template

import signal

from app.database import load_user_settings, get_user_theme, get_color_themes
from . import bp

@bp.route('/')
def index():
    print(get_user_theme())

    return render_template("index.html", userSettings=load_user_settings(),
                           theme=get_user_theme())

@bp.route('/about')
def about():
    return render_template("misc/about.html", userSettings=load_user_settings(),
                           theme=get_user_theme())

@bp.route('/settings')
def settings():
    return render_template('misc/settings.html', userSettings=load_user_settings(),
                           theme=get_user_theme(), colorThemes=get_color_themes())

@bp.route('/shutdown')
def shutdown():
    signal.raise_signal(signal.SIGINT)  # Sending signal to run.py to que destruction of the thread, & de-initializing

    return render_template("misc/shutdown.html")
