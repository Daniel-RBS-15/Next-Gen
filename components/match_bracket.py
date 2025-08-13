"""
Match Bracket Component

This module provides the MatchBracketComponent class for creating individual
match brackets and tournament progression visualization.
"""
import os

from dash import html
from typing import Optional, Tuple, Dict


class MatchBracketComponent:
    """
    Renders individual match brackets with VS indicators and progression lines.
    
    This class handles the creation of match brackets that show team matchups,
    winners, and progression through the tournament rounds.
    """

    def __init__(self, color_scheme: Dict[str, str]):
        """
        :param color_scheme:
        Initialize the match bracket component.

        Args:
            color_scheme (Dict[str, str]): Color mapping for different team groups
        """
        self.color_scheme = color_scheme

    @staticmethod
    def create_match_bracket(team1: str,
                             team2: str,
                             winner: Optional[str] = None,
                             match_id: str = "",
                             round_name: str = "") -> html.Div:

        """
        Create a match bracket showing two teams facing off.

        Args:
            team1 (str): First team name
            team2 (str): Second team name
            winner (Optional[str]): Winner of the match (if determined)
            match_id (str): Unique identifier for the match
            round_name (str): Name of the tournament round

        Returns:
            html.Div: Dash HTML component representing the match bracket
        """
        #  Determine styling based on match status
        bracket_classes = ["match-bracket"]
        if winner:
            bracket_classes.append("match-completed")
        else:
            bracket_classes.append("match-pending")

        return html.Div([
            html.Div([
                html.Div(team1, className="team-slot team-slot-1"),
                html.Div("VS", className="vs-indicator"),
                html.Div(team2, className="team-slot team-slot-2")
            ], className="match-teams"),

            html.Div([
                html.Div(winner or "TBD", className="match-winner")
            ], className="match-result") if round_name != "Quarter Finals" else None

        ],
            className=" ".join(bracket_classes),
            id=f"match-{match_id}")

    def create_quarter_final_bracket(self,
                                     qf_name: str,
                                     team1: str,
                                     team2: str,
                                     background_color_1: str,
                                     background_color_2: str,
                                     team1_logo: Optional[str] = None,
                                     team2_logo: Optional[str] = None,
                                     ) -> html.Div:
        """
        Create a quarter-final specific bracket layout.
        
        Args:
            qf_name (str): Quarter-final identifier (QF1, QF2, etc.)
            team1 (str): First team name
            team2 (str): Second team name
            background_color_1 (str): Background color for QF1
            background_color_2 (str): Background color for QF2
            team1_logo (str): Team 1 logo
            team2_logo (str): Team 2 logo
            
        Returns:
            html.Div: Quarter-final bracket component
        """
        background_color_1 = self.color_scheme.get(background_color_1, "#CCCCCC")
        background_color_2 = self.color_scheme.get(background_color_2, "#CCCCCC")
        if team1_logo and team2_logo:
            return html.Div([
                html.Div(qf_name, className="qf-label"),
                html.Div([
                    html.Div([
                        html.Span(str(1), className="team-position"),
                        html.Img(src=team1_logo, className="qf-logo qf-logo-1"),
                    ],
                        className="qf-team qf-team-1",
                        style={
                            "backgroundColor": background_color_1,
                            "border": f"2px solid {background_color_1}"
                        }
                    ),
                    html.Div("VS", className="qf-vs"),
                    html.Div(
                        [
                            html.Span(str(2), className="team-position"),
                            html.Img(src=team2_logo, className="qf-logo qf-logo-2"),
                        ],
                        className="qf-team qf-team-2",
                        style={
                            "backgroundColor": background_color_2,
                            "border": f"2px solid {background_color_2}"
                        }
                    )
                ], className="qf-matchup")
            ], className="quarter-final-bracket")
        else:
            return html.Div([
                html.Div(qf_name, className="qf-label"),
                html.Div([
                    html.Div([
                        html.Span(str(1), className="team-position"),
                        html.Div(team1, className="qf-text qf-text-1"),
                    ],
                        className="qf-team qf-team-1",
                        style={
                            "backgroundColor": background_color_1,
                            "border": f"2px solid {background_color_1}"
                        }
                    ),
                    html.Div("VS", className="qf-vs"),
                    html.Div(
                        [
                            html.Span(str(2), className="team-position"),
                            html.Div(team2, className="qf-text qf-text-2")
                        ],
                        className="qf-team qf-team-2",
                        style={
                            "backgroundColor": background_color_2,
                            "border": f"2px solid {background_color_2}"
                        }
                    )
                ], className="qf-matchup")
            ], className="quarter-final-bracket")

    def create_semin_final_bracket(self,
                                   sf_name: str,
                                   team1: str,
                                   team2: str,
                                   background_color_1: str,
                                   background_color_2: str,
                                   team1_logo: Optional[str] = None,
                                   team2_logo: Optional[str] = None,
                                   ) -> html.Div:
        """
        Create a semi-final specific bracket layout.

        Args:
            sf_name (str): Quarter-final identifier (QF1, QF2, etc.)
            team1 (str): First team name
            team2 (str): Second team name
            background_color_1 (str): Background color for QF1
            background_color_2 (str): Background color for QF2
            team1_logo (str): Team 1 logo
            team2_logo (str): Team 2 logo


        Returns:
            html.Div: Quarter-final bracket component
        """
        background_color_1 = self.color_scheme.get(background_color_1, "#CCCCCC")
        background_color_2 = self.color_scheme.get(background_color_2, "#CCCCCC")
        if team1_logo and team2_logo:
            return html.Div([
                html.Div(sf_name, className="sf-label"),
                html.Div([
                    html.Div([
                        html.Img(src=team1_logo, className="sf-logo sf-logo-1"),
                    ],
                        className="sf-team sf-team-1",
                        style={
                            "backgroundColor": background_color_1,
                            "border": f"2px solid {background_color_1}"
                        }
                    ),
                    html.Div("VS", className="sf-vs"),
                    html.Div(
                        [
                            html.Img(src=team2_logo, className="sf-logo sf-logo-2"),
                        ],
                        className="sf-team sf-team-2",
                        style={
                            "backgroundColor": background_color_2,
                            "border": f"2px solid {background_color_2}"
                        }
                    )
                ], className="sf-matchup")
            ], className="semi-final-bracket")
        else:
            return html.Div([
                html.Div(sf_name, className="sf-label"),
                html.Div([
                    html.Div([
                        html.Div(team1, className="sf-text sf-text-1"),
                    ],
                        className="sf-team sf-team-1",
                        style={
                            "backgroundColor": background_color_1,
                            "border": f"2px solid {background_color_1}"
                        }
                    ),
                    html.Div("VS", className="sf-vs"),
                    html.Div(
                        [
                            html.Div(team2, className="sf-text sf-text-2")
                        ],
                        className="sf-team sf-team-2",
                        style={
                            "backgroundColor": background_color_2,
                            "border": f"2px solid {background_color_2}"
                        }
                    )
                ], className="sf-matchup")
            ], className="semi-final-bracket")

    @staticmethod
    def create_progression_line(start_pos: Tuple[int, int],
                                end_pos: Tuple[int, int],
                                line_type: str = "horizontal") -> html.Div:
        """
        Create a progression line connecting matches.
        
        Args:
            start_pos (Tuple[int, int]): Starting position (x, y)
            end_pos (Tuple[int, int]): Ending position (x, y)
            line_type (str): Type of line ("horizontal", "vertical", "bracket")
            
        Returns:
            html.Div: Progression line component
        """
        line_classes = ["progression-line", f"line-{line_type}"]

        # Calculate line positioning and dimensions
        x1, y1 = start_pos
        x2, y2 = end_pos

        if line_type == "horizontal":
            width = abs(x2 - x1)
            height = 2
            left = min(x1, x2)
            top = y1
        elif line_type == "vertical":
            width = 2
            height = abs(y2 - y1)
            left = x1
            top = min(y1, y2)
        else:  # bracket type
            width = abs(x2 - x1)
            height = abs(y2 - y1)
            left = min(x1, x2)
            top = min(y1, y2)

        return html.Div(
            className=" ".join(line_classes),
            style={
                "position": "absolute",
                "left": f"{left}px",
                "top": f"{top}px",
                "width": f"{width}px",
                "height": f"{height}px",
                "backgroundColor": "#333"
            }
        )

    @staticmethod
    def create_final_bracket(
            team1: str,
            team2: str,
            team1_logo: Optional[str] = None,
            team2_logo: Optional[str] = None
    ) -> html.Div:
        """
        Create the final match bracket with trophy styling.
        
        Args:
            team1 (str): First finalist
            team2 (str): Second finalist
            team1_logo (Optional[str], optional): First finalist logo
            team2_logo (Optional[str], optional): Second finalist logo
            
        Returns:
            html.Div: Final bracket with trophy decoration
        """
        if team1_logo and team2_logo:
            return html.Div([
                html.Div("🏆", className="trophy-icon"),
                html.Div([
                    html.Img(src=team1_logo, className="finalist-logo"),
                    html.Div("VS", className="final-vs"),
                    html.Img(src=team2_logo, className="finalist-logo")
                ], className="final-matchup"),
                # html.Div("Final", className="final-label"),
                html.Div("🏆", className="trophy-icon")
            ], className="final-bracket")
        else:
            return html.Div([
                html.Div("🏆", className="trophy-icon"),
                html.Div([
                    html.Div(team1, className="finalist finalist-1"),
                    html.Div("VS", className="final-vs"),
                    html.Div(team2, className="finalist finalist-2")
                ], className="final-matchup"),
                # html.Div("Final", className="final-label"),
                html.Div("🏆", className="trophy-icon")
            ], className="final-bracket")

    @staticmethod
    def create_placement_bracket(
            placement: str,
            team1: str,
            team2: str,
            team1_logo: Optional[str] = None,
            team2_logo: Optional[str] = None
    ) -> html.Div:
        """
        Create a placement match bracket (3rd-4th, 5th-8th, etc.).
        
        Args:
            placement (str): Placement description (e.g., "3rd-4th", "5th-8th")
            team1 (str): First team
            team2 (str): Second team
            team1_logo (Optional[str], optional): First team logo
            team2_logo (Optional[str], optional): Second team logo
            
        Returns:
            html.Div: Placement bracket component
        """
        if team1_logo and team2_logo:
            return html.Div([
                html.Div(placement, className="placement-label"),
                html.Div([
                    html.Img(src=team1_logo, className="placement-team-logo"),
                    html.Div("VS", className="placement-vs"),
                    html.Img(src=team2_logo, className="placement-team-logo")
                ], className="placement-matchup")
            ], className="placement-bracket")
        else:
            return html.Div([
                html.Div(placement, className="placement-label"),
                html.Div([
                    html.Div(team1, className="placement-team"),
                    html.Div("VS", className="placement-vs"),
                    html.Div(team2, className="placement-team")
                ], className="placement-matchup")
            ], className="placement-bracket")

    @staticmethod
    def create_placement_bracket_matches(
            placement: str,
            team1: str,
            team2: str,
            team1_logo: Optional[str] = None,
            team2_logo: Optional[str] = None,
            match_status: Optional[str] = None,
    ) -> html.Div:
        """
        Create a placement match bracket (3rd-4th, 5th-8th, etc.).

        Args:
            placement (str): Placement description (e.g., "3rd-4th", "5th-8th")
            team1 (str): First team
            team2 (str): Second team
            team1_logo (Optional[str], optional): First team logo
            team2_logo (Optional[str], optional): Second team logo
            match_status (Optional[str], optional): Match status

        Returns:
            html.Div: Placement bracket component
        """
        match_bracket_element = []
        if match_status == 'live':
            match_bracket_element.append(html.Span(className="live-dot"))
        if team1_logo and team2_logo:
            match_bracket_element += [
                html.Img(src=team1_logo, className="tournament-matches placement-team-logo"),
                html.Div("VS", className="tournament-matches placement-vs"),
                html.Img(src=team2_logo, className="tournament-matches placement-team-logo")
            ]
        else:
            match_bracket_element += [
                html.Div(team1, className="tournament-matches placement-team"),
                html.Div("VS", className="tournament-matches placement-vs"),
                html.Div(team2, className="tournament-matc  hes placement-team")
            ]
        return html.Div(match_bracket_element, className="tournament-matches placement-matchup")
