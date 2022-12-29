import matplotlib.pyplot as plt
import seaborn as sns


def my_two_side_barplot(df, number_of_clubs):
    # Two-sided barplot
    sns.set_theme(style='whitegrid')

    fig, ax = plt.subplots(1, 1, figsize=(4, 5))

    ax = sns.barplot(data=df, y='club', x='player',
                     orient="h", linewidth=0.3, edgecolor='black', facecolor='lightgray')

    ax = sns.barplot(data=df, y='club', x='goals',
                     orient="h", linewidth=0.3, edgecolor='black', facecolor='orange')

    plt.xlabel(None)
    plt.title("Comparison of number of players and goals")
    plt.tick_params(axis='both', which='major', labelsize=6)

    for num, p in enumerate(ax.patches):
        print(num, p)
        if num == 0:
            text = " PLAYERS: %d" % -p.get_width()
        elif num < number_of_clubs:
            text = " %d" % -p.get_width()
        elif num == number_of_clubs:
            text = " GOALS: %d" % p.get_width()
        else:
            text = " %d" % p.get_width()
        ax.annotate(text, xy=(p.get_width(), p.get_y() + p.get_height() / 2),
                    fontsize=5, ha="left", va="center")

    plt.xticks([])
    plt.subplots_adjust(left=0.2, right=0.9)
    plt.savefig('out/comparison_of_clubs.png')
    plt.show()
