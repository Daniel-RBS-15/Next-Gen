"""
Team Card Component

This module provides the TeamCardRenderer class for creating individual team
display cards in the tournament visualization.
"""

from dash import html
from typing import Dict, Optional  # , Any


class TeamCardRenderer:
    """
    Renders individual team cards with consistent styling and layout.
    
    This class handles the creation of team display cards that show team names,
    colors, and status indicators throughout the tournament bracket.
    """

    def __init__(self, color_scheme: Dict[str, str]):
        """
        Initialize the team card renderer.
        
        Args:
            color_scheme (Dict[str, str]): Color mapping for different team groups
        """
        self.color_scheme = color_scheme

    def create_team_card(self,
                         team_name: str,
                         team_color: str,
                         position: int = 1,
                         is_winner: bool = False,
                         is_eliminated: bool = False,
                         card_size: str = "normal",
                         team_logo: Optional[str] = None) -> html.Div:
        """
        Create a team card component.
        
        Args:
            team_name (str): Display name of the team
            team_color (str): Color identifier for the team
            position (int): Position number within the team card
            is_winner (bool): Whether this team is a winner
            is_eliminated (bool): Whether this team is eliminated
            card_size (str): Size variant ("small", "normal", "large")
            team_logo (Optional[str]): Team logo
            
        Returns:
            html.Div: Dash HTML component representing the team card
        """
        # Determine card styling based on status
        card_classes = ["team-card", f"team-card-{card_size}"]

        if is_winner:
            card_classes.append("team-card-winner")
        elif is_eliminated:
            card_classes.append("team-card-eliminated")

        # Get color from scheme
        background_color = self.color_scheme.get(team_color, "#CCCCCC")

        if team_logo:
            return html.Div([
                html.Div([
                    html.Span(str(position), className="team-position"),
                    html.Img(src=team_logo, className="team-logo"),
                    html.Span(team_name, className="team-name")
                ], className="team-card-content")
            ],
                className=" ".join(card_classes),
                style={
                    "backgroundColor": background_color,
                    "border": f"2px solid {background_color}"
                })
        else:
            return html.Div([
                html.Div([
                    html.Span(str(position), className="team-position"),
                    html.Span(team_name, className="team-name")
                ], className="team-card-content")
            ],
                className=" ".join(card_classes),
                style={
                    "backgroundColor": background_color,
                    "border": f"2px solid {background_color}"
                })

    def create_group_header(self, group_name: str, group_color: str) -> html.Div:
        """
        Create a group header component.
        
        Args:
            group_name (str): Name of the group (e.g., "Group A", "Group 9-12")
            group_color (str): Color identifier for the group
            
        Returns:
            html.Div: Dash HTML component for the group header
        """
        background_color = self.color_scheme.get(group_color, "#CCCCCC")

        return html.Div([
            html.H3(group_name, className="group-title")
        ],
            className="group-header",
            style={
                "backgroundColor": background_color,
                "color": "white"
            })

    def create_team_group(self, group_name: str, teams: list, group_color: str) -> html.Div:
        """
        Create a complete team group with header and team cards.
        
        Args:
            group_name (str): Name of the group
            teams (list): List of team data
            group_color (str): Color identifier for the group
            
        Returns:
            html.Div: Complete group component with header and teams
        """
        group_header = self.create_group_header(group_name, group_color)

        team_cards = [
            self.create_team_card(
                team.name,
                team.color,
                team.position,
                team.is_winner,
                team.is_eliminated,
                team_logo=team.team_logo
            ) for team in teams
        ]

        return html.Div([
            group_header,
            html.Div(team_cards, className="team-group-cards")
        ], className="team-group")
