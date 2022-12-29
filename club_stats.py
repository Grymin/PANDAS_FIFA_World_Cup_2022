from my_two_side_barplot import my_two_side_barplot
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px


def club_stats():
    """Analyses of the club player results (clubs with > 10 players in the World Cup)"""

    dfps = pd.read_csv('in/player_stats.csv')
    dfps.info(verbose=True)

    dfps_club = dfps.groupby('club').agg({'player': 'count',
                                          'games': 'sum',
                                          'goals': 'sum',
                                          'assists': 'sum'
                                          })
    dfps_club.sort_values(by=['player', 'goals'], ascending=False, inplace=True)

    dfps_club = dfps_club[dfps_club.player >= 10].reset_index()
    number_of_clubs = dfps_club.shape[0]

    # Switch players to negative axis
    dfps_club.loc[:, 'player'] = -dfps_club.loc[:, 'player']

    # Sort
    dfps_club.sort_values(by='goals')

    my_two_side_barplot(dfps_club, number_of_clubs)