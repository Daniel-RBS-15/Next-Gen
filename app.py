"""
Tournament Tree Visualization - Main Application

This is the main entry point for the tournament tree visualization Dash application.
It initializes the app, sets up layouts, and registers callbacks for interactivity.

Usage:
    python app.py

The application will start on http://localhost:8050 by default.
"""

import dash
from dash import html
import dash_bootstrap_components as dbc

# Import application modules
from layouts.main_layout import MainLayoutManager
from callbacks.rotation_callbacks import register_rotation_callbacks
from config.app_config import (
    APP_TITLE, APP_HOST, APP_PORT, DEBUG_MODE
)

# Initialize Dash app with Bootstrap theme
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title=APP_TITLE,
    update_title=None,
    suppress_callback_exceptions=True
)

# Configure app server
server = app.server


class TournamentVisualizationApp:
    """
    Main application class for the tournament visualization.
    
    This class orchestrates the setup of layouts, callbacks, and
    configuration for the complete tournament visualization system.
    """

    def __init__(self):
        """Initialize the tournament visualization app."""
        self.app = app
        self.layout_manager = MainLayoutManager()
        self.setup_app()

    def setup_app(self):
        """Set up the complete application configuration."""
        self.configure_layout()
        self.register_callbacks()
        self.configure_meta_tags()

    def configure_layout(self):
        """Configure the main application layout."""
        self.app.layout = html.Div([
            # Main application layout
            self.layout_manager.create_app_layout()
        ])

    def register_callbacks(self):
        """Register all application callbacks."""
        # Register rotation callbacks
        register_rotation_callbacks(self.app, self.layout_manager)

        # Additional callbacks can be registered here
        self.register_additional_callbacks()

    def register_additional_callbacks(self):
        """
        Register additional callbacks for enhanced functionality.
        
        This method can be extended to add more interactive features
        such as team selection, match result updates, etc.
        """
        # Placeholder for future callback registrations
        pass

    def configure_meta_tags(self):
        """Configure meta tags for the application."""
        self.app.index_string = '''
        <!DOCTYPE html>
        <html>
            <head>
                {%metas%}
                <title>{%title%}</title>
                {%favicon%}
                {%css%}
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta name="description" content="Interactive tournament tree visualization with rotating views">
                <meta name="keywords" content="tournament, bracket, visualization, sports, competition">
            </head>
            <body>
                {%app_entry%}
                <footer>
                    {%config%}
                    {%scripts%}
                    {%renderer%}
                </footer>
            </body>
        </html>
        '''

    def run(self, host=None, port=None, debug=None):
        """
        Run the Dash application.
        
        Args:
            host (str, optional): Host to run on. Defaults to config value.
            port (int, optional): Port to run on. Defaults to config value.
            debug (bool, optional): Debug mode. Defaults to config value.
        """
        self.app.run(
            host=host or APP_HOST,
            port=port or APP_PORT,
            debug=debug if debug is not None else DEBUG_MODE
        )


def create_app():
    """
    Factory function to create and configure the tournament app.
    
    Returns:
        TournamentVisualizationApp: Configured application instance
    """
    return TournamentVisualizationApp()


tournament_app = create_app()
# Main execution
if __name__ == "__main__":
    tournament_app.run()
