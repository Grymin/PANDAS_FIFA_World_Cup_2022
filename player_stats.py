from my_ax_barplot import my_ax_barplot

import matplotlib.pyplot as plt
import pandas as pd


def player_stats():
    """Polish player stats"""

    dfps = pd.read_csv('in/player_stats.csv')
    dfps.info()

    # change age format from years-days to float
    age_temp_df = dfps.age.str.split('-', expand=True).astype(int)
    dfps.age = age_temp_df.loc[:, 0] + age_temp_df.loc[:, 1]/365
    dfps.sort_values(by='age', inplace=True, ascending=False)
    dfps_pol = dfps[dfps.team == 'Poland'].loc[:, ['player', 'minutes', 'age', 'goals', 'assists']]
    dfps_pol.sort_values(by='minutes', ascending=False, inplace=True)

    # graphs
    fig, axs = plt.subplots(1, 4, figsize=(12, 5), sharey="row", squeeze=True, )

    my_ax_barplot(axs[0], dfps_pol, series_x='player', series_y='minutes', label='Minutes')
    my_ax_barplot(axs[1], dfps_pol, series_x='player', series_y='age', label='Age')
    my_ax_barplot(axs[2], dfps_pol, series_x='player', series_y='goals', label='Goals')
    my_ax_barplot(axs[3], dfps_pol, series_x='player', series_y='assists', label='Assists')

    for ax in axs:
        ax.set_ylabel(None)
        # ax.set_xticks([])

    plt.tight_layout(w_pad=0)
    plt.savefig('out/polish_players')

    plt.show()