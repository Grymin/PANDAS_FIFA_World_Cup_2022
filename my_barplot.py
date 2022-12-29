import matplotlib.pyplot as plt
import os
import seaborn as sns


def my_barplot(df, series_x, series_y, title="X_LABEL_TO_SET",
               sort=False, show=False, asc=True):
    """Definition of personal barplot in seaborn"""

    team_counter = df.loc[:, series_y].count()

    # Sorting the values
    if sort:
        df.sort_values(by=series_y, inplace=True, ascending=asc)
        df.reset_index(drop=True, inplace=True)

    # Choosing proper indexes of min/max/pol values
    max_val = max(df.loc[:, series_y])
    min_val = min(df.loc[:, series_y])
    max_index = df.loc[:, series_y][df.loc[:, series_y] == max_val].index.tolist()
    min_index = df.loc[:, series_y][df.loc[:, series_y] == min_val].index.tolist()
    pol_index = df.loc[:, series_x][df.loc[:, series_x] == 'Poland'].index.tolist()
    avg_val = df.loc[:, series_y].mean()

    # Setting colors
    clrs = ['orange' if (y == 'Poland')
            else 'lightgray'
            for y in df.loc[:, series_x]]

    # Setting width (larger for min/max/pol
    width = [0.8 if (x == min_val or x == max_val) else 0.2 for x in df.loc[:, series_y]]

    # Graph
    fig = plt.subplots(figsize=(4, 5))
    ax = sns.barplot(data=df, x=series_y, y=series_x, orient="h", linewidth=width, edgecolor='black', palette=clrs)
    sns.lineplot(x=[avg_val, avg_val], y=[-0.5, team_counter - 0.5], color='black')
    plt.xlabel(None)
    plt.title(title)
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.subplots_adjust(left=0.2, right=0.9)
    plt.xlim(0, max_val * 1.2)
    for num, p in enumerate(ax.patches):
        if num in min_index:
            ax.annotate(" MIN: %.1f" % p.get_width(), xy=(p.get_width(), p.get_y() + p.get_height() / 2),
                        fontsize=5, ha="left", va="center")
        elif num in max_index:
            ax.annotate(" MAX: %.1f" % p.get_width(), xy=(p.get_width(), p.get_y() + p.get_height() / 2),
                        fontsize=5, ha="left", va="center")
        elif num in pol_index:
            ax.annotate(" POL: %.1f" % p.get_width(), xy=(p.get_width(), p.get_y() + p.get_height() / 2),
                        fontsize=5, color='orange', ha="left", va="center")

    # Save
    out_dir = 'out'
    if not (os.path.isdir(out_dir)):
        os.mkdir(out_dir)

    plt.savefig(os.path.join(out_dir, f'{title}.png'))
    if show:
        plt.show()
    else:
        plt.close()
