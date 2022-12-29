from team_analysis import team_analysis
from club_stats import club_stats
from player_stats import player_stats

import numpy as np
import os
import pandas as pd
import seaborn as sns

print(os.listdir('in'))
team_analysis()
club_stats()
player_stats()


