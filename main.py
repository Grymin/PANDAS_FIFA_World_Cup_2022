from team_analysis import team_analysis
from club_stats import club_stats
from player_stats import player_stats

import os

# List of files
print(os.listdir('in'))

# Procedures for the analyses:

# - analyses of each country team
team_analysis()

# - analyses of the clubs the most players where from
club_stats()

# - analyses of the polish players
player_stats('Poland')
player_stats('Argentina')
player_stats('France')



