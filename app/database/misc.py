import json

from .paths import COLOR_THEMES_PATH


def get_color_themes() -> dict:
    with open(COLOR_THEMES_PATH, "r") as file:
        return json.load(file)
