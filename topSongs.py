#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import six

col_list = ["artist", "song", "album", "popularity"]
df = pd.read_csv("top50_songs.csv", usecols=col_list)

print(df.head())

def render_mpl_table(data, col_width=35.0, row_height=1, font_size=14, header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',bbox=[0,0,1,1], header_columns=0, ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0,1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors)])
    plt.savefig('top50_songs_table.jpg', bbox_inches="tight")
    return ax

render_mpl_table(df, header_columns=0, col_width=2.0)
