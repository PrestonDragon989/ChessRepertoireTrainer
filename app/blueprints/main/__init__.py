from flask import Blueprint

import os

bp = Blueprint('main_blueprint',
               __name__,
               root_path=os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')),
               template_folder="templates",
               static_folder="static"
               )

from . import routes
