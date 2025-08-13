"""
Tournament Data Models and Sample Data

This module contains the data structures and sample data for the tournament
visualization, based on the provided tournament tree sketch.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass

import pandas as pd

from data_reader.NextGenDataReader import NextGenDataReader


@dataclass
class TeamData:
    """Represents a team in the tournament."""
    name: str
    group: str
    color: str
    position: int
    is_winner: bool = False
    is_eliminated: bool = False
    team_logo: Optional[str] = None


@dataclass
class MatchData:
    """Represents a match between two teams."""
    match_id: str
    team1: str
    team2: str
    winner: Optional[str] = None
    round_name: str = ""
    position: tuple = (0, 0),
    team1_logo: Optional[str] = None
    team2_logo: Optional[str] = None,
    match_number: Optional[int] = None,
    match_pitch: Optional[int] = None,
    match_score: Optional[str] = None,
    match_time: Optional[str] = None,
    match_status: Optional[str] = None


GROUP_COLORS = {
    "A": "orange",
    "B": "blue",
    "C": "pink",
    "D": "green",
}

ROUND_NAMES_MAPPING = {
    "group_stageA1": "A1",
    "group_stageA5": "A5",
    "group_stageA9": "A9",
    "group_stageB2": "B2",
    "group_stageB6": "B6",
    "group_stageB10": "B10",
    "group_stageC3": "C3",
    "group_stageC7": "C7",
    "group_stageC11": "C11",
    "group_stageD4": "D4",
    "group_stageD8": "D8",
    "group_stageD12": "D12",
    # "group_stageC": "C",
    # "group_stageD": "D",
    "quarter_final_1": "QF1",
    "quarter_final_2": "QF2",
    "quarter_final_3": "QF3",
    "quarter_final_4": "QF4",
    "semi_final_1": "SF1",
    "semi_final_2": "SF2",
    "9th-12th_round_19th-12th Place Group17": '9-12-17',
    "9th-12th_round_19th-12th Place Group18": '9-12-18',
    "9th-12th_round_29th-12th Place Group22": '9-12-22',
    "9th-12th_round_29th-12th Place Group23": '9-12-23',
    "9th-12th_round_39th-12th Place Group25": '9-12-25',
    "9th-12th_round_39th-12th Place Group26": '9-12-26',
    "5th-8th_place_1": '5-8-1',
    "5th-8th_place_2": '5-8-2',
    "7th-8th_place": "7-8",
    "5th-6th_place": "5-6",
    "3rd-4th_place": "3rd-4th",
    "final": "Final"
}


# Sample tournament data based on the sketch
# SAMPLE_TEAMS = {
#     # Group 9-12 teams
#     "Team 9": TeamData("LOREM IPSUM", "9-12", "orange", 3),
#     "Team 10": TeamData("LOREM IPSUM", "9-12", "blue", 3),
#     "Team 11": TeamData("LOREM IPSUM", "9-12", "pink", 3),
#     "Team 12": TeamData("LOREM IPSUM", "9-12", "green", 3),
#
#     # Group A teams
#     "Team A1": TeamData("LOREM IPSUM", "A", "orange", 1),
#     "Team A2": TeamData("LOREM IPSUM", "A", "orange", 2),
#     "Team A3": TeamData("LOREM IPSUM", "A", "orange", 3),
#
#     # Group B teams
#     "Team B1": TeamData("LOREM IPSUM", "B", "blue", 1),
#     "Team B2": TeamData("LOREM IPSUM", "B", "blue", 2),
#     "Team B3": TeamData("LOREM IPSUM", "B", "blue", 3),
#
#     # Group C teams
#     "Team C1": TeamData("LOREM IPSUM", "C", "pink", 1),
#     "Team C2": TeamData("LOREM IPSUM", "C", "pink", 2),
#     "Team C3": TeamData("LOREM IPSUM", "C", "pink", 3),
#
#     # Group D teams
#     "Team D1": TeamData("LOREM IPSUM", "D", "green", 1),
#     "Team D2": TeamData("LOREM IPSUM", "D", "green", 2),
#     "Team D3": TeamData("LOREM IPSUM", "D", "green", 3),
# }
next_gen_reader = NextGenDataReader()
fixtures_df = next_gen_reader.read_next_gen_fixtures()
group_standings = next_gen_reader.read_next_gen_group_standings()
SAMPLE_TEAMS = {
    row['team_id']: TeamData(
        row['team_name'],
        row['group_name'],
        GROUP_COLORS[row['group_name']],
        row["group_position"],
        False,
        False,
        f"assets/images/team_logos/{row['team_id']}.png",
    )
    for ix, row in group_standings.iterrows()
}


def format_result(home_team_goals, away_team_goals, home_penalty_goals=None, away_penalty_goals=None):
    if pd.isna(home_team_goals):
        home_team_goals = ''

    if pd.isna(away_team_goals):
        away_team_goals = ''

    main_result = str(home_team_goals) + ':' + str(away_team_goals)
    if pd.notna(home_penalty_goals) or pd.notna(away_penalty_goals ):
        main_result += ' (' + str(home_penalty_goals) + ':' + str(away_penalty_goals) + ')'

    return main_result


def format_match_key(round_name, group_name, match_id):
    match_key = round_name + str(group_name).replace('None', '')
    if round_name in ['group_stage', '9th-12th_round_1', '9th-12th_round_2', '9th-12th_round_3']:
        match_key += str(match_id)
    return match_key


SAMPLE_MATCHES = {
    ROUND_NAMES_MAPPING[
        format_match_key(row['round_name'], row['group_name'], row['match_id'])
    ]:
    MatchData(
        ROUND_NAMES_MAPPING[format_match_key(row['round_name'], row['group_name'], row['match_id'])],
        row['home_team_name'],
        row['away_team_name'],
        None,
        row["round_name"],
        (0, 0),
        f"assets/images/team_logos/{row['home_team_id']}.png" if pd.notna(row['home_team_id']) else 'assets/images/fallback.png',
        f"assets/images/team_logos/{row['away_team_id']}.png" if pd.notna(row['away_team_id']) else 'assets/images/fallback.png',
        row['match_id'],
        row['pitch'],
        format_result(row['home_team_goals'], row['away_team_goals'], row['home_team_penalty_goals'], row['away_team_penalty_goals']),
        row['match_time'],
        row['match_status'],
    )
    for _, row in fixtures_df.iterrows()
}

GOALSCORERS = next_gen_reader.read_top_goalscorers()


def get_tournament_structure() -> Dict:
    """
    Returns the complete tournament structure with teams and matches.
    
    Returns:
        Dict: Complete tournament data structure
    """
    return {
        "teams": SAMPLE_TEAMS,
        "matches": SAMPLE_MATCHES,
        "groups": ["9-12", "A", "B", "C", "D"],
        "rounds": ["Quarter Finals", "Semi Finals", "Final", "Placement"]
    }


def get_teams_by_group(group: str) -> List[TeamData]:
    """
    Get all teams in a specific group.
    
    Args:
        group (str): Group identifier
        
    Returns:
        List[TeamData]: List of teams in the group
    """
    return [team for team in SAMPLE_TEAMS.values() if team.group == group]


def get_matches_by_round(round_name: str) -> List[MatchData]:
    """
    Get all matches in a specific round.
    
    Args:
        round_name (str): Round name
        
    Returns:
        List[MatchData]: List of matches in the round
    """
    return [match for match in SAMPLE_MATCHES.values() if match.round_name == round_name]


print('')
