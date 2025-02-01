// Dictionary of all the html element ID's to the user python dictionary Keys
export const idToKey = {
    "color-theme": "color_theme",
    "piece-style": "piece_style",
    "board-theme": "board_theme",
    "show-notation-during-training": "show_notation_during_training",
    "show-variation-name-during-training": "show_variation_name_during_training",
    "show-annotation-glyphs-during-training": "show_annotation_glyphs_during_training",
    "show-move-comments-during-training": "show_move_comments_during_training",
    "mute": "mute",
    "display-name": "display_name"
};

// Collects all of the dropdown menus (and single textbox) by id
export const elements = {};
for (const [id, key] of Object.entries(idToKey)) {
    elements[id] = document.getElementById(id);    
}

// Used to import all of the user's settings into the dropdowns
export function importUserSettingsIntoUI(userSettings) {
    for (const [id, key] of Object.entries(idToKey)) {
        elements[id].value = userSettings[key];
    }
}

export async function sendNewUserData(userData, key, newValue) {    
    userData[key] = newValue;

    try {
        // Send POST request to Flask endpoint
        const response = await fetch('/api/update_user_settings', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'  // Tell server we're sending JSON
            },
            body: JSON.stringify(userData)          // Convert JavaScript object to JSON string
        });

        // Check if the response was successful
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Handle Response (Error or Success)
        const result = await response.json();
        console.log('Server responded:', result, `Data Changed: ${key} => ${newValue}`);
    } catch (error) {
        console.error('Error sending data:', error);
    }
}