from typing import List

from dash import html

from components.match_bracket import MatchBracketComponent
from components.team_card import TeamCardRenderer
from config.tournament_config import TEAM_COLORS, TOURNAMENT_GROUPS
from data.tournament_data import get_tournament_structure, get_teams_by_group, MatchData


class TournamentMatchesComponent:
    def __init__(self):
        self.team_renderer = TeamCardRenderer(TEAM_COLORS)
        self.match_renderer = MatchBracketComponent(TEAM_COLORS)
        self.tournament_data = get_tournament_structure()

    @staticmethod
    def create_matches_header() -> html.Div:
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
            html.Div(main_groups, className="tournament-matches-main-groups")
        ], className="tournament-matches group-section")

    def create_group_stage_matches(self) -> html.Div:
        group_matches_ids = ['A1', 'A5', 'A9', 'B2', 'B6', 'B10', 'C3', 'C7', 'C11', 'D4', 'D8', 'D12']
        group_stage_matches = [
            match_data
            for match, match_data in self.tournament_data["matches"].items()
            if match in group_matches_ids
        ]
        table = self.create_table(title='Thursday, 15th August 2024', matches=group_stage_matches)

        return table

    def create_knockout_matches_1(self) -> html.Div:
        group_matches_ids = [
            'QF1', 'QF2', 'QF3', 'QF4',
            '9-12-17', '9-12-18', '9-12-22', '9-12-23',
            '5-8-1', '5-8-2',
            'SF1', 'SF2'
        ]
        group_stage_matches = [
            match_data
            for match, match_data in self.tournament_data["matches"].items()
            if match in group_matches_ids
        ]
        table = self.create_table(title='Friday, 16th August 2024', matches=group_stage_matches)

        return table

    def create_knockout_matches_2(self) -> html.Div:
        group_matches_ids = [
            '9-12-25', '9-12-26',
            '7-8', '5-6',
            '3rd-4th',
            'Final'
        ]
        group_stage_matches = [
            match_data
            for match, match_data in self.tournament_data["matches"].items()
            if match in group_matches_ids
        ]
        table = self.create_table(title='Saturday, 17th August 2024', matches=group_stage_matches)

        return table

    def create_table(self, title: str, matches: List[MatchData], class_name_suffix: int = 1) -> html.Div:
        table_rows = []

        table_header = [
            html.Thead(
                html.Tr([
                    html.Th("Match", className=f"table-header-cell-match-id-header{class_name_suffix}"),
                    html.Th("Pitch", className=f"table-header-cell-pitch-header{class_name_suffix}"),
                    # html.Th("Group", className="table-header-cell"),
                    html.Th("Time", className=f"table-header-cell-time-header{class_name_suffix}"),
                    html.Th("Fixture", className=f"table-header-cell-fixture-header{class_name_suffix}"),
                    html.Th("Result", className=f"table-header-cell-result-header{class_name_suffix}")
                    ])
                )
        ]

        for match in matches:
            if match.team1_logo and match.team2_logo:
                table_rows.append(
                    html.Tr([
                        html.Td(match.match_number, className=f"table-body-cell{class_name_suffix}"),
                        html.Td(match.match_pitch, className=f"table-body-cell{class_name_suffix}"),
                        # html.Td(match.group, className="table-body-cell"),
                        html.Td(match.match_time, className=f"table-body-cell{class_name_suffix}"),
                        html.Td(
                            html.Div([
                                self.match_renderer.create_placement_bracket_matches(
                                    placement="",
                                    team1=match.team1,
                                    team2=match.team2,
                                    team1_logo=match.team1_logo,
                                    team2_logo=match.team2_logo,
                                    match_status=match.match_status
                                ),
                                html.Div([match.team1 + ' vs ' + match.team2],
                                         className=f"table-body-cell fixture-cell-text{class_name_suffix}")
                            ], className=f"table-body-cell fixture-cell-container{class_name_suffix}"),
                            className=f"table-body-cell-fixture-cell-images{class_name_suffix}"),
                        html.Td(match.match_score, className=f"table-body-cell result-cell{class_name_suffix}")
                    ], className=f"table-body-row-tr{class_name_suffix}")
                )
            else:
                table_rows.append(
                    html.Tr([
                        html.Td(match.match_number, className=f"table-body-cell{class_name_suffix}"),
                        html.Td(match.match_pitch, className=f"table-body-cell{class_name_suffix}"),
                        # html.Td(match.group, className="table-body-cell"),
                        html.Td(match.match_time, className=f"table-body-cell{class_name_suffix}"),
                        html.Td(html.Div(match.team1 + ' vs ' + match.team2,  className=f"table-body-cell fixture-cell-text{class_name_suffix}"),
                                className=f"table-body-cell fixture-cell{class_name_suffix}"),
                        html.Td(match.match_score, className=f"table-body-cell result-cell{class_name_suffix}")
                    ], className=f"table-body-row-tr{class_name_suffix}")
                )

        table_body = [html.Tbody(table_rows)]

        return html.Div([
            html.Div([
                html.Div(title, className=f"table-section-title{class_name_suffix}"),
            ], className=f"table-title-container{class_name_suffix}"),
            html.Table(table_header + table_body, className=f"tournament-table{class_name_suffix}")
        ], className=f"table-container-wrapper{class_name_suffix}")

    def create_complete_tournament_matches(self) -> html.Div:
        """
        Create the complete tournament matches layout.

        Returns:
            html.Div: Complete tournament visualization
        """
        return html.Div([
            self.create_matches_header(),

            html.Div([
                html.Div([
                    self.create_group_section(),
                    self.create_group_stage_matches(),
                ], className="tournament-matches-groups"
                ),
                html.Div([
                    self.create_knockout_matches_1(),
                    self.create_knockout_matches_2(),
                ], className="tournament-matches-knockouts")
            ], className="tournament-matches-body")

        ], className="tournament-matches-container"
        )

