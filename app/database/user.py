from json import load, dump

from .paths import USER_SETTINGS_PATH

import os.path as path


_SAMPLE_USER = {
    "board_theme": "light_and_dark_brown",
    "color_theme": "light",
    "display_name": "Sample User",
    "mute": "false",
    "piece_style": "cburnett",
    "show_annotation_glyphs_during_training": "false",
    "show_eval": "after",
    "show_move_comments_during_training": "false",
    "show_notation_during_training": "true",
    "show_variation_name_during_training": "true"
}


def load_user_settings() -> dict:
    # Checking to see if the user file exists yet, and if not creates one with the basic sample settings
    if not path.exists(USER_SETTINGS_PATH):
        with open(USER_SETTINGS_PATH, "w") as file:
            dump(SAMPLE_USER, file)

    # Returns user settings dictionary
    with open(USER_SETTINGS_PATH, "r") as file:
        return load(file)


def dump_user_settings(new_user_settings: dict) -> None:
    # Gets user settings
    with open(USER_SETTINGS_PATH, "w") as file:
        return dump(new_user_settings, file)
