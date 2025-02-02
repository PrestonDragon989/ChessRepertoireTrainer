from flask import request, jsonify, json
import json

from app.database import dump_user_settings

from . import bp

@bp.route('/update_user_settings', methods=['POST'])
def change_user_settings():
    """
    API Call to change the settings of a user
    :return: End Status
    """
    try:
        # Get raw data from request
        raw_data = request.get_json()

        # Convert to dictionary if needed
        if isinstance(raw_data, str):
            new_user_settings = json.loads(raw_data)
        elif isinstance(raw_data, dict):
            new_user_settings = raw_data
        else:
            raise ValueError("Invalid data format received")

        # Writing new Settings to the user's file
        dump_user_settings(new_user_settings)

        # Return Code Handling
        return jsonify({'status': 'success', 'message': 'Data properly received.'})

    except KeyError as e:
        return jsonify({'status': 'error', 'message': f'Missing required field: {str(e)}'}), 400
    except json.JSONDecodeError:
        return jsonify({'status': 'error', 'message': 'Invalid JSON format'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400