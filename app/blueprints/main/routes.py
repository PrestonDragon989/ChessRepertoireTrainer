from flask import render_template

import signal

from . import bp

@bp.route('/')
def index():
    return render_template("index.html")

@bp.route('/about')
def about():
    return render_template("misc/about.html")

@bp.route('/shutdown')
def shutdown():
    signal.raise_signal(signal.SIGINT)

    return render_template("misc/shutdown.html")
