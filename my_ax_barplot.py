import seaborn as sns


def my_ax_barplot(spec_ax, df, series_x, series_y, label, coloring='by_values'):
    """
    Returning ax to subplot with data
    :param spec_ax: specific ax to print on
    :param df: figure with data
    :param series_x: name of the column with categories
    :param series_y: name of the column with values
    :param label: name as the x-label
    :param coloring: name of the country to color
    :return: specific ax with data
    """

    # Indexes with the given country name / max / min
    max_val = max(df.loc[:, series_y])
    min_val = min(df.loc[:, series_y])
    max_val_index = df.loc[df.loc[:, series_y] == max_val].index.tolist()
    min_val_index = df.loc[df.loc[:, series_y] == min_val].index.tolist()
    pol_index = df.loc[df.loc[:, series_x] == coloring].index.tolist()
    indexes_to_value = max_val_index + min_val_index + pol_index
    indexes_to_value = list(set(indexes_to_value))  # remove duplicates

    # Colors to give to bars
    clrs = ['orange' if (df.at[i, series_x] == coloring)
            else 'red' if df.at[i, series_y] == max_val
            else 'lightgreen' if df.at[i, series_y] == min_val
            else 'lightgray'
            for i in df.index]

    sns.barplot(ax=spec_ax, data=df, y=series_x, x=series_y,
                orient="h", linewidth=0.3, edgecolor='black', palette=clrs)

    spec_ax.tick_params(axis='both', which='major', labelsize=6)
    spec_ax.set_xlabel(label)
    spec_ax.set_ylabel(None)

    for num, p in enumerate(spec_ax.patches):
        if p.get_width() > 0 and num in indexes_to_value:
            spec_ax.annotate(" %d" % p.get_width(), xy=(p.get_width(), p.get_y() + p.get_height() / 2),
                             fontsize=6, color='black', ha='right', va='center')

    return spec_ax
