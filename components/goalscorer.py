import pandas as pd
from dash import html


class GoalScorerComponent:
    def __init(self, goalscorers: pd.DataFrame):
        self.goalscorers = goalscorers

    @staticmethod
    def create_player_card(team_id: int, player_name: str) -> html.Div:
        team_logo = f"assets/images/team_logos/{team_id}.png"
        return html.Div([
            html.Img(src=team_logo, className="goalscorer-table team-logo"),
            html.Div(player_name, className="goalscorer-table player-name"),
        ], className="goalscorer-table player-card"
        )

    def create_goalscorer_table(self, players: pd.DataFrame) -> html.Div:
        table_rows = []

        table_header = [
            html.Thead(
                html.Tr([
                    html.Th("Place", className=f"goalscorer-table-header-cell-place-header"),
                    html.Th("Player", className=f"goalscorer-table-header-cell-player-header"),
                    # html.Th("Team", className=f"goalscorer-table-header-cell-team-header"),
                    html.Th("Goals", className=f"goalscorer-table-header-cell-goals-header")
                ]), className="goalscorer-table goalscorer-table-header"
            )
        ]

        for _, player in players.iterrows():
            table_rows.append(
                html.Tr([
                    html.Td(str(player.place), className=f"goalscorer-table-body-cell"),
                    html.Td(
                        html.Div([
                            self.create_player_card(
                                team_id=player.team_id,
                                player_name=player.player_name,
                            ),
                        ], className=f"goalscorer-table-body-cell player-cell-container"),
                        className=f"goalscorer-table-body-cell-player-cell-images"),
                    # html.Td(player.team_name, className=f"goalscorer-table-body-cell"),
                    html.Td(str(player.total_goals), className=f"goalscorer-table-body-cell")
                ], className=f"goalscorer-table-body-row-tr")
            )

        table_body = [html.Tbody(table_rows)]

        return html.Div([
            html.Table(table_header + table_body, className=f"goalscorer-tournament-table")
        ], className=f"goalscorer-table-container-wrapper")
