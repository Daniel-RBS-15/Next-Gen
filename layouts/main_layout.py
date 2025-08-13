"""
Main Layout Module

This module provides the main application layout and view management for the
tournament tree visualization Dash application.
"""

from dash import html
from dash import dcc

from components.tournament_goalscorers import TournamentGoalscorersComponent
from components.tournament_matches import TournamentMatchesComponent
from components.tournament_tree import TournamentTreeComponent
# from config.app_config import VIEW_DISPLAY_NAMES, AVAILABLE_VIEWS


class MainLayoutManager:
    """
    Manages the main application layout and view switching.
    
    This class handles the overall application structure, including the header,
    main content area, and view rotation controls.
    """
    
    def __init__(self):
        """Initialize the main layout manager."""
        self.tournament_tree = TournamentTreeComponent()
        self.tournament_matches = TournamentMatchesComponent()
        self.goalscorers = TournamentGoalscorersComponent()
    
    @staticmethod
    def create_app_header() -> html.Div:
        """
        Create the application header with navigation controls.
        
        Returns:
            html.Div: Application header component
        """
        return html.Div([
            html.Div([
                html.H1("Tournament Visualization", className="app-title"),
                html.Div([
                    html.Span("Auto-rotating views", className="rotation-status"),
                    html.Button("⏸️", id="rotation-toggle", className="rotation-button")
                ], className="rotation-controls")
            ], className="header-content")
        ], className="app-header")
    
    @staticmethod
    def create_view_indicator() -> html.Div:
        """
        Create the current view indicator.
        
        Returns:
            html.Div: View indicator component
        """
        return html.Div([
            html.Div(id="current-view-name", className="current-view"),
            html.Div([
                html.Div(className="progress-dot active"),
                html.Div(className="progress-dot"),
                html.Div(className="progress-dot")
            ], className="view-progress")
        ], className="view-indicator")
    
    def create_tournament_tree_view(self) -> html.Div:
        return self.tournament_tree.create_complete_tournament_tree()

    def create_tournament_matches_view(self) -> html.Div:
        return self.tournament_matches.create_complete_tournament_matches()

    def create_goal_scorers_view(self) -> html.Div:
        return self.goalscorers.create_goalscorers_tables()

    @staticmethod
    def create_tournament_table_view() -> html.Div:
        """
        Create the tournament table view layout.
        
        Returns:
            html.Div: Tournament table view
        """
        return html.Div([
            html.H2("next generation trophy 25/26", className="view-title"),
            html.Div([
                html.Table([
                    html.Thead([
                        html.Tr([
                            html.Th("Match"),
                            html.Th("Team 1"),
                            html.Th("Team 2"),
                            html.Th("Round"),
                            html.Th("Status")
                        ])
                    ]),
                    html.Tbody([
                        html.Tr([
                            html.Td("QF1"),
                            html.Td("Team A1"),
                            html.Td("Team C3"),
                            html.Td("Quarter Finals"),
                            html.Td("Pending")
                        ]),
                        html.Tr([
                            html.Td("QF2"),
                            html.Td("Team B1"),
                            html.Td("Team D3"),
                            html.Td("Quarter Finals"),
                            html.Td("Pending")
                        ]),
                        html.Tr([
                            html.Td("QF3"),
                            html.Td("Team C1"),
                            html.Td("Team A3"),
                            html.Td("Quarter Finals"),
                            html.Td("Pending")
                        ]),
                        html.Tr([
                            html.Td("QF4"),
                            html.Td("Team D1"),
                            html.Td("Team B3"),
                            html.Td("Quarter Finals"),
                            html.Td("Pending")
                        ])
                    ])
                ], className="tournament-table")
            ], className="table-container")
        ], className="tournament-table-view")
    
    @staticmethod
    def create_statistics_view() -> html.Div:
        """
        Create the statistics view layout.
        
        Returns:
            html.Div: Statistics view
        """
        return html.Div([
            html.H2("next generation trophy 25/26", className="view-title"),
            html.Div([
                html.Div([
                    html.H3("Teams by Group"),
                    html.Div([
                        html.Div([
                            html.Span("Group A: ", className="stat-label"),
                            html.Span("3 teams", className="stat-value")
                        ], className="stat-item"),
                        html.Div([
                            html.Span("Group B: ", className="stat-label"),
                            html.Span("3 teams", className="stat-value")
                        ], className="stat-item"),
                        html.Div([
                            html.Span("Group C: ", className="stat-label"),
                            html.Span("3 teams", className="stat-value")
                        ], className="stat-item"),
                        html.Div([
                            html.Span("Group D: ", className="stat-label"),
                            html.Span("3 teams", className="stat-value")
                        ], className="stat-item")
                    ], className="stats-grid")
                ], className="stats-section"),
                
                html.Div([
                    html.H3("Tournament Progress"),
                    html.Div([
                        html.Div([
                            html.Span("Matches Completed: ", className="stat-label"),
                            html.Span("0/15", className="stat-value")
                        ], className="stat-item"),
                        html.Div([
                            html.Span("Current Round: ", className="stat-label"),
                            html.Span("Quarter Finals", className="stat-value")
                        ], className="stat-item")
                    ], className="stats-grid")
                ], className="stats-section")
            ], className="statistics-content")
        ], className="statistics-view")
    
    def create_main_content_area(self) -> html.Div:
        """
        Create the main content area with view switching.
        
        Returns:
            html.Div: Main content area
        """
        return html.Div([
            # Hidden stores for state management
            dcc.Store(id="current-view-store", data="tournament_tree"),
            dcc.Store(id="rotation-enabled-store", data=True),
            
            # View content container
            html.Div(id="view-content", children=[
                self.create_tournament_tree_view()  # default view
                # self.create_tournament_matches_view()
                # self.create_goal_scorers_view()
            ]),
            
            # Rotation timer
            dcc.Interval(
                id="rotation-timer",
                interval=10000,  # 30 seconds
                n_intervals=1
            )
        ], className="main-content")
    
    def create_app_layout(self) -> html.Div:
        """
        Create the complete application layout.
        
        Returns:
            html.Div: Complete app layout
        """
        return html.Div([
            # self.create_app_header(),
            # self.create_view_indicator(),
            self.create_main_content_area()
        ], className="app-container")
