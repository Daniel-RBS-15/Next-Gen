import pandas as pd
from dash import html

from .goalscorer import GoalScorerComponent
from data.tournament_data import GOALSCORERS


class TournamentGoalscorersComponent:
    def __init__(self, top_n: int = 14):
        self.players = GOALSCORERS.head(n=top_n)
        self.goalscorer_renderer = GoalScorerComponent()

    @staticmethod
    def create_matches_header() -> html.Div:
        """
        Create the tournament header with title.

        Returns:
            html.Div: Tournament header component
        """
        return html.Div([
            html.H2("next generation trophy 25/26", className="tournament-title")
        ], className="tournament-header-goalscorers")

    def create_goalscorers_tables(self):
        midpoint = len(self.players) // 2
        df1 = self.players.iloc[:midpoint]
        df2 = self.players.iloc[midpoint:]

        tables = [
            self.goalscorer_renderer.create_goalscorer_table(players=df1),
            self.goalscorer_renderer.create_goalscorer_table(players=df2)
        ]

        return html.Div([
            self.create_matches_header(),
            html.Div(tables, className="goalscorer-body")
        ], className="tournament-goalscorers-container")
