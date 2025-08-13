"""
Tournament Tree Component

This module provides the TournamentTreeComponent class for creating the complete
tournament bracket visualization based on the provided sketch design.
"""
from typing import List

from dash import html
from .team_card import TeamCardRenderer
from .match_bracket import MatchBracketComponent
from config.tournament_config import TEAM_COLORS, TOURNAMENT_GROUPS
from data.tournament_data import get_tournament_structure, get_teams_by_group, SAMPLE_MATCHES


class TournamentTreeComponent:
    """
    Main component for rendering the complete tournament tree visualization.
    
    This class orchestrates the layout of team groups, match brackets, and
    progression lines to create the full tournament bracket as shown in the sketch.
    """

    def __init__(self):
        """Initialize the tournament tree component."""
        self.team_renderer = TeamCardRenderer(TEAM_COLORS)
        self.match_renderer = MatchBracketComponent(TEAM_COLORS)
        self.tournament_data = get_tournament_structure()

    @staticmethod
    def create_tournament_header() -> html.Div:
        """
        Create the tournament header with title.

        Returns:
            html.Div: Tournament header component
        """
        return html.Div([
            html.H2("next generation trophy 25/26", className="tournament-title")
        ], className="tournament-header")

    def create_group_section(self) -> html.Div:
        """
        Create the group stage section with all team groups.
        
        Returns:
            html.Div: Complete group section layout
        """
        # groups_layout = []

        # Main groups (A, B, C, D)
        main_groups = []
        for group_id in ["A", "B", "C", "D"]:
            group_teams = get_teams_by_group(group_id)
            group_color = TOURNAMENT_GROUPS[group_id]["color"]
            group_component = self.team_renderer.create_team_group(
                f"Group {group_id}", group_teams, group_color
            )
            main_groups.append(group_component)

        return html.Div([
            # html.Div([group_9_12], className="side-group"),
            html.Div(main_groups, className="main-groups")
        ], className="group-section")

    def create_quarter_finals_section(self) -> html.Div:
        """
        Create the quarter-finals section.
        
        Returns:
            html.Div: Quarter-finals layout
        """
        qf_brackets = [
            self.match_renderer.create_quarter_final_bracket(
                SAMPLE_MATCHES["QF1"].match_id, SAMPLE_MATCHES["QF1"].team1, SAMPLE_MATCHES["QF1"].team2,
                background_color_1='orange', background_color_2='blue',
                team1_logo=SAMPLE_MATCHES["QF1"].team1_logo, team2_logo=SAMPLE_MATCHES["QF1"].team2_logo,
            ),
            self.match_renderer.create_quarter_final_bracket(
                SAMPLE_MATCHES["QF2"].match_id, SAMPLE_MATCHES["QF2"].team1, SAMPLE_MATCHES["QF2"].team2,
                background_color_1='blue', background_color_2='orange',
                team1_logo=SAMPLE_MATCHES["QF2"].team1_logo, team2_logo=SAMPLE_MATCHES["QF2"].team2_logo,
            ),
            self.match_renderer.create_quarter_final_bracket(
                SAMPLE_MATCHES["QF3"].match_id, SAMPLE_MATCHES["QF3"].team1, SAMPLE_MATCHES["QF3"].team2,
                background_color_1='pink', background_color_2='green',
                team1_logo=SAMPLE_MATCHES["QF3"].team1_logo, team2_logo=SAMPLE_MATCHES["QF3"].team2_logo,
            ),
            self.match_renderer.create_quarter_final_bracket(
                SAMPLE_MATCHES["QF4"].match_id, SAMPLE_MATCHES["QF4"].team1, SAMPLE_MATCHES["QF4"].team2,
                background_color_1='green', background_color_2='pink',
                team1_logo=SAMPLE_MATCHES["QF4"].team1_logo, team2_logo=SAMPLE_MATCHES["QF4"].team2_logo,
            )
        ]

        return html.Div([
            html.Div([qf_brackets[0], qf_brackets[1]], className="qf-left"),
            html.Div([qf_brackets[2], qf_brackets[3]], className="qf-right")
        ], className="quarter-finals-section")

    def create_semi_finals_section(self) -> html.Div:
        """
        Create the semi-finals section.
        
        Returns:
            html.Div: Semi-finals layout
        """
        sf_brackets = [
            self.match_renderer.create_semin_final_bracket(
                SAMPLE_MATCHES["SF1"].match_id, SAMPLE_MATCHES["SF1"].team1, SAMPLE_MATCHES["SF1"].team2,
                background_color_1='None', background_color_2='None',
                team1_logo=SAMPLE_MATCHES["SF1"].team1_logo, team2_logo=SAMPLE_MATCHES["SF1"].team2_logo,
            ),
            self.match_renderer.create_semin_final_bracket(
                SAMPLE_MATCHES["SF2"].match_id, SAMPLE_MATCHES["SF2"].team1, SAMPLE_MATCHES["SF2"].team2,
                background_color_1='None', background_color_2='None',
                team1_logo=SAMPLE_MATCHES["SF2"].team1_logo, team2_logo=SAMPLE_MATCHES["SF2"].team2_logo
            ),
        ]

        return html.Div([
            html.Div([sf_brackets[0]], className="semi-final-top"),
            html.Div([sf_brackets[1]], className="semi-final-bottom")
        ], className="semi-finals-section")

    def create_finals_section(self) -> html.Div:
        """
        Create the finals section with trophy.
        
        Returns:
            html.Div: Finals layout
        """
        final_bracket = self.match_renderer.create_final_bracket(
            SAMPLE_MATCHES["Final"].team1, SAMPLE_MATCHES["Final"].team2,
            team1_logo=SAMPLE_MATCHES["Final"].team1_logo, team2_logo=SAMPLE_MATCHES["Final"].team2_logo
        )

        placement_3rd_4th = self.match_renderer.create_placement_bracket(
            "3rd-4th", SAMPLE_MATCHES["3rd-4th"].team1, SAMPLE_MATCHES["3rd-4th"].team2,
            team1_logo=SAMPLE_MATCHES["3rd-4th"].team1_logo, team2_logo=SAMPLE_MATCHES["3rd-4th"].team2_logo
        )

        return html.Div([
            final_bracket,
            placement_3rd_4th
        ], className="finals-section")

    def create_placement_section(
            self,
            match_1_name: str,
            match_2_name: str,
            match_1_teams: List[str],
            match_2_teams: List[str],
    ) -> html.Div:
        """
        Create the placement matches section (5th-8th, etc.).
        
        Returns:
            html.Div: Placement matches layout
        """
        placement_brackets = [
            self.match_renderer.create_placement_bracket(
                match_1_name, match_1_teams[0], match_1_teams[1]
            ),
            self.match_renderer.create_placement_bracket(
                match_2_name, match_2_teams[0], match_2_teams[1]
            )
        ]

        return html.Div(placement_brackets, className="placement-section")

    def create_complete_tournament_tree(self) -> html.Div:
        """
        Create the complete tournament tree layout.
        
        Returns:
            html.Div: Complete tournament visualization
        """
        group_9_12_teams = get_teams_by_group("9-12")
        group_9_12 = self.team_renderer.create_team_group(
            "Group 9-12", group_9_12_teams, "indigo"
        )

        return html.Div([
            self.create_tournament_header(),

            html.Div([
                # Left side: Group Stage
                html.Div([
                    self.create_group_section(),
                ], className="tournament-left"),

                # Center Left: Quarter Finals & 9-12
                html.Div([
                    self.create_quarter_finals_section(),
                    # html.Div([group_9_12], className="side-group"),
                ], className="tournament-center-left"),
                html.Div([
                    self.create_semi_finals_section(),
                    # self.create_placement_section(
                    #     match_1_name="Placement (5th-8th) Match 1", match_2_name="Placement (5th-8th) Match 2",
                    #     match_1_teams=["Loser QF1", "Loser QF3"], match_2_teams=["Loser QF2", "Loser QF4"]
                    # )
                ], className="tournament-center-right"),

                # Right side: Placement matches
                html.Div([
                    self.create_finals_section(),
                    # self.create_placement_section(
                    #     match_1_name="5th-6th", match_2_name="7th-8th",
                    #     match_1_teams=["Winner Placement 1", "Winner Placement 2"],
                    #     match_2_teams=["Loser Placement 1", "Loser Placement 2"]
                    # )
                ], className="tournament-right")

            ], className="tournament-body")

        ], className="tournament-tree-container")
