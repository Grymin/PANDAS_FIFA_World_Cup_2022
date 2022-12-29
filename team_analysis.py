from my_ax_barplot import my_ax_barplot
import matplotlib.pyplot as plt
import pandas as pd


def team_analysis():
    """ Analyses of each national team results"""

    # DF TEAM ANALYSIS
    df_team = pd.read_csv('in/team_data.csv')
    df_team.info(verbose=True)

    # Additional columns
    df_team["offsides_per_game"] = df_team["offsides"] / df_team["games"]
    df_team["fouls_per_game"] = df_team["fouls"] / df_team["games"]
    df_team["shots_on_target_per_game"] = df_team["shots_on_target"] / df_team["games"]
    df_team["touches_per_game"] = df_team["touches"] / df_team["games"]
    df_team["dribbles_completed_per_game"] = df_team["dribbles_completed"] / df_team["games"]

    # Graphs
    fig, axs = plt.subplots(2, 3, figsize=(12, 10), sharey='all')
    axs[0, 0] = my_ax_barplot(axs[0, 0], df_team, "team", "avg_age", label="Average age", coloring="Poland")
    axs[0, 1] = my_ax_barplot(axs[0, 1], df_team, "team", "offsides_per_game", label="Offsides per match", coloring="Poland")
    axs[0, 2] = my_ax_barplot(axs[0, 2], df_team, "team", "fouls_per_game", label="Fouls per match", coloring="Poland")
    axs[1, 0] = my_ax_barplot(axs[1, 0], df_team, "team", "shots_on_target_per_game", label="Shots on target per match", coloring="Poland")
    axs[1, 1] = my_ax_barplot(axs[1, 1], df_team, "team", "touches_per_game", label="Touches per match", coloring="Poland")
    axs[1, 2] = my_ax_barplot(axs[1, 2], df_team, "team", "dribbles_completed_per_game", label="Completed dribbles per match", coloring="Poland")

    for row in axs:
        for ax in row:
            ax.set_ylabel(None)

    plt.tight_layout(w_pad=0, h_pad=3)
    plt.savefig('out/teams_comparison')

    plt.show()
