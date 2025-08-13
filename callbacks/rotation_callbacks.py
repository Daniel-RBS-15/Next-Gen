"""
Rotation Callbacks Module

This module provides callback functions for automatic view rotation and
manual view switching in the tournament visualization app.
"""

from dash import Input, Output, State
from dash.exceptions import PreventUpdate
from dash import html
from layouts.main_layout import MainLayoutManager
from config.app_config import AVAILABLE_VIEWS, VIEW_DISPLAY_NAMES


class RotationCallbackManager:
    """
    Manages callbacks for view rotation and switching functionality.

    This class handles the automatic rotation between different views
    (tournament tree, schedule, goalscorers) and provides manual controls.
    """

    def __init__(self, app, layout_manager: MainLayoutManager):
        """
        Initialize the rotation callback manager.

        Args:
            app: Dash application instance
            layout_manager (MainLayoutManager): Layout manager instance
        """
        self.app = app
        self.layout_manager = layout_manager
        self.register_callbacks()

    def register_callbacks(self):
        """Register all rotation-related callbacks."""
        self.register_view_rotation_callback()
        # self.register_rotation_toggle_callback()
        self.register_view_content_callback()
        # self.register_view_indicator_callback()

    def register_view_rotation_callback(self):
        """
        Register callback for automatic view rotation.

        This callback triggers every 30 seconds to switch between views
        when auto-rotation is enabled.
        """
        @self.app.callback(
            Output('current-view-store', 'data'),
            [Input('rotation-timer', 'n_intervals'),
             State('current-view-store', 'data'),
             State('rotation-enabled-store', 'data')],
        )
        def rotate_views(n_intervals, current_view, rotation_enabled):
            """
            Automatically rotate between available views.

            Args:
                n_intervals (int): Number of timer intervals elapsed
                current_view (str): Currently active view
                rotation_enabled (bool): Whether auto-rotation is enabled

            Returns:
                str: Next view to display
            """
            # Allow initial update even if n_intervals is 0 to set the first view
            if n_intervals is None:
                raise PreventUpdate

            if not rotation_enabled and n_intervals > 0:
                raise PreventUpdate

            try:
                current_index = AVAILABLE_VIEWS.index(current_view)
                next_index = (current_index + 1) % len(AVAILABLE_VIEWS)
                return AVAILABLE_VIEWS[next_index]
            except ValueError:
                # If current view not found, default to first view
                return AVAILABLE_VIEWS[0]

    def register_rotation_toggle_callback(self):
        """
        Register callback for toggling auto-rotation on/off.

        This callback handles the play/pause button for rotation control.
        """
        @self.app.callback(
            [Output('rotation-enabled-store', 'data'),
             Output('rotation-toggle', 'children'),
             Output('rotation-timer', 'disabled')],
            [Input('rotation-toggle', 'n_clicks')],
            [State('rotation-enabled-store', 'data')]
        )
        def toggle_rotation(n_clicks, rotation_enabled):
            """
            Toggle auto-rotation on or off.

            Args:
                n_clicks (int): Number of button clicks
                rotation_enabled (bool): Current rotation state

            Returns:
                tuple: (new_rotation_state, button_text, timer_disabled)
            """
            if n_clicks is None:
                raise PreventUpdate

            new_state = not rotation_enabled
            button_text = "▶️" if not new_state else "⏸️"
            timer_disabled = not new_state

            return new_state, button_text, timer_disabled

    def register_view_content_callback(self):
        """
        Register callback for updating view content based on current view.

        This callback switches the main content area between different views.
        """
        @self.app.callback(
            Output('view-content', 'children'),
            [Input('current-view-store', 'data')]
        )
        def update_view_content(current_view):
            """
            Update the main content area based on the current view.

            Args:
                current_view (str): Currently selected view

            Returns:
                html.Div: Content for the selected view
            """
            if current_view == "tournament_tree":
                return self.layout_manager.create_tournament_tree_view()
            elif current_view == "tournament_schedule":
                return self.layout_manager.create_tournament_matches_view()
            elif current_view == "goalscorers":
                return self.layout_manager.create_goal_scorers_view()
            else:
                # Default to tournament tree view
                return self.layout_manager.create_tournament_tree_view()

    def register_view_indicator_callback(self):
        """
        Register callback for updating the view indicator.

        This callback updates the current view name and progress dots.
        """
        @self.app.callback(
            [Output('current-view-name', 'children'),
             Output('view-progress', 'children')],
            [Input('current-view-store', 'data')]
        )
        def update_view_indicator(current_view):
            """
            Update the view indicator with current view information.

            Args:
                current_view (str): Currently selected view

            Returns:
                tuple: (view_name, progress_dots)
            """
            # Get display name for current view
            view_name = VIEW_DISPLAY_NAMES.get(current_view, "Unknown View")
            
            # Create progress dots
            progress_dots = []
            for i, view in enumerate(AVAILABLE_VIEWS):
                dot_classes = ["progress-dot"]
                if view == current_view:
                    dot_classes.append("active")
                
                progress_dots.append(
                    html.Div(className=" ".join(dot_classes))
                )
            
            return view_name, progress_dots


def register_rotation_callbacks(app, layout_manager: MainLayoutManager):
    """
    Convenience function to register all rotation callbacks.
    
    Args:
        app: Dash application instance
        layout_manager (MainLayoutManager): Layout manager instance
        
    Returns:
        RotationCallbackManager: Configured callback manager
    """
    return RotationCallbackManager(app, layout_manager)

