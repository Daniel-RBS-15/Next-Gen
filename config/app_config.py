"""
Application Configuration Settings

This module contains all the configuration settings for the tournament tree
visualization Dash application.
"""

# Application Settings
APP_TITLE = "NEXT GENERATION TROPHY 25/26"
APP_HOST = "0.0.0.0"
APP_PORT = 8060
DEBUG_MODE = True

# View Rotation Settings
ROTATION_INTERVAL_SECONDS = 30
AUTO_ROTATION_ENABLED = True

# Available Views
AVAILABLE_VIEWS = [
    "tournament_tree",
    "tournament_schedule",
    "goalscorers",
]

# View Display Names
VIEW_DISPLAY_NAMES = {
    "tournament_tree": "Tournament Tree",
    "tournament_schedule": "Tournament Schedule",
    "goalscorers": "Goalscorers"
}

# Layout Settings
CONTAINER_MAX_WIDTH = "1400px"
HEADER_HEIGHT = "80px"
FOOTER_HEIGHT = "40px"
