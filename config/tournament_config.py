"""
Tournament Configuration Settings

This module contains tournament-specific configuration including team data,
groups, and tournament structure.
"""

# Team Colors (matching the sketch design)
TEAM_COLORS = {
    # "orange": "#FF8C00",
    "pink": "#D2003C",
    # "blue": "#4A90E2",
    "green": "#790C27",

    # "pink": "#E91E63",
    "orange": "#0E39FF",
    # "green": "#8BC34A",
    "blue": "#001D46",
    "indigo": "#3F51B5"
}

# Tournament Groups
TOURNAMENT_GROUPS = {
    "A": {
        "teams": ["Team A1", "Team A2", "Team A3"],
        "color": "orange"
    },
    "B": {
        "teams": ["Team B1", "Team B2", "Team B3"], 
        "color": "blue"
    },
    "C": {
        "teams": ["Team C1", "Team C2", "Team C3"],
        "color": "pink"
    },
    "D": {
        "teams": ["Team D1", "Team D2", "Team D3"],
        "color": "green"
    },
    "9-12": {
        "teams": ["Team 9", "Team 10", "Team 11", "Team 12"],
        "color": "indigo"
    }
}

# Tournament Structure
TOURNAMENT_ROUNDS = [
    "Group Stage",
    "Quarter Finals", 
    "Semi Finals",
    "Finals",
    "Placement Matches"
]

# Match Structure
QUARTER_FINALS = ["QF1", "QF2", "QF3", "QF4"]
SEMI_FINALS = ["SF1", "SF2"]
FINALS = ["Final"]
PLACEMENT_MATCHES = ["3rd-4th", "5th-8th"]

