from google.cloud import bigquery

from utils import get_gcp_credentials

fixture_team_name_placeholder = {
    1: {"home": "", "away": ""},
    2: {"home": "", "away": ""},
    3: {"home": "", "away": ""},
    4: {"home": "", "away": ""},
    5: {"home": "", "away": ""},
    6: {"home": "", "away": ""},
    7: {"home": "", "away": ""},
    8: {"home": "", "away": ""},
    9: {"home": "", "away": ""},
    10: {"home": "", "away": ""},
    11: {"home": "", "away": ""},
    12: {"home": "", "away": ""},

    13: {"home": "1. Group A", "away": "2. Group B"},
    14: {"home": "1. Group B", "away": "2. Group A"},
    15: {"home": "1. Group C", "away": "2. Group D"},
    16: {"home": "1. Group D", "away": "2. Group C"},

    17: {"home": "3. Group A", "away": "3. Group C"},
    18: {"home": "3. Group B", "away": "3. Group D"},

    19: {"home": "Winner Match 13", "away": "Winner Match 15"},
    20: {"home": "Winner Match 14", "away": "Winner Match 16"},

    21: {"home": "Loser Match 13", "away": "Loser Match 15"},
    22: {"home": "3. Group C", "away": "3. Group B"},

    23: {"home": "3. Group D", "away": "3. Group A"},
    24: {"home": "Loser Match 14", "away": "Loser Match 16"},

    25: {"home": "3. Group A", "away": "3. Group B"},
    26: {"home": "3. Group C", "away": "3. Group D"},

    27: {"home": "Loser Match 21", "away": "Loser Match 24"},

    28: {"home": "Winner Match 21", "away": "Winner Match 24"},

    29: {"home": "Loser Match 19", "away": "Loser Match 20"},

    30: {"home": "Winner Match 19", "away": "Winner Match 20"},
}


class NextGenDataReader:
    def __init__(self):
        self.gcp_client = bigquery.Client(credentials=get_gcp_credentials())
        self.project_id = "apds-fc-salzburg-plygnd"
        self.dataset_id = "90_mart_sandbox"

    def read_next_gen_fixtures(self):
        fixtures_query = f"""
        SELECT * FROM `{self.project_id}.{self.dataset_id}.mrt_next_gen_all_fixtures`
"""
        fixtures_df = self.gcp_client.query(fixtures_query).to_dataframe()

        fixtures_df["home_team_name"] = fixtures_df["home_team_name"].mask(
            fixtures_df["home_team_name"].isna(),
            fixtures_df["match_id"].map(lambda x: fixture_team_name_placeholder[x]["home"])
        )
        fixtures_df["away_team_name"] = fixtures_df["away_team_name"].mask(
            fixtures_df["away_team_name"].isna(),
            fixtures_df["match_id"].map(lambda x: fixture_team_name_placeholder[x]["away"])
        )

        return fixtures_df

    def read_next_gen_group_standings(self):
        groups_query = f"""SELECT * FROM `{self.project_id}.{self.dataset_id}.mrt_next_gen_group_standings`"""
        group_standings_df = self.gcp_client.query(groups_query).to_dataframe()
        return group_standings_df

    def read_top_goalscorers(self):
        goalscorers_query = f"""SELECT * FROM `{self.project_id}.{self.dataset_id}.mrt_next_gen_top_goalscorers`"""
        goalscorers_df = self.gcp_client.query(goalscorers_query).to_dataframe()
        return goalscorers_df
