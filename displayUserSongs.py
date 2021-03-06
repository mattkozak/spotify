#!/usr/bin/env python3

import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# load in the data file #
with open("top50_data.txt") as json_file:
    data = json.load(json_file)

# initialize empty lists #
list_of_results = data[0]["items"]
list_of_artist_names = []
list_of_artist_uri = []
list_of_song_names = []
list_of_song_uri = []
list_of_durations_ms = []
list_of_explicit = []
list_of_albums = []
list_of_popularity = []

# loop through each result and populate empty lists #
for result in list_of_results:
    result["album"]
    this_artists_name = result["artists"][0]["name"]
    list_of_artist_names.append(this_artists_name)
    this_artists_uri = result["artists"][0]["uri"]
    list_of_artist_uri.append(this_artists_uri)
    list_of_songs = result["name"]
    list_of_song_names.append(list_of_songs)
    song_uri = result["uri"]
    list_of_song_uri.append(song_uri)
    list_of_duration = result["duration_ms"]
    list_of_durations_ms.append(list_of_duration)
    song_explicit = result["explicit"]
    list_of_explicit.append(song_explicit)
    this_album = result["album"]["name"]
    list_of_albums.append(this_album)
    song_popularity = result["popularity"]
    list_of_popularity.append(song_popularity)

# create a pandas data frame #
all_songs = pd.DataFrame(
    {'artist': list_of_artist_names,
    'artist_uri': list_of_artist_uri,
    'song': list_of_song_names,
    'song_uri': list_of_song_names,
    'duration_ms': list_of_durations_ms,
    'explicit': list_of_explicit,
    'album': list_of_albums,
    'popularity': list_of_popularity
    })

# export song list to csv file #
all_songs_saved = all_songs.to_csv('top50_songs.csv')
top50 = all_songs

# display songs in descending order #
descending_order = top50['artist'].value_counts().sort_values(ascending=False).index
ax = sb.countplot(y = top50['artist'], order=descending_order)

# configure plot #
sb.despine(fig=None, ax=None, top=True, right=True, left=False, trim=False)
sb.set(rc={'figure.figsize':(6,7.2)})

# set axis labels #
#ax.setylabel('')
#ax.setxlabel('')
ax.set_title('Songs per Artist in Top 50', fontsize=16, fontweight='heavy')
sb.set(font_scale = 1.4)
ax.axes.get_xaxis().set_visible(False)
ax.set_frame_on(False)

# do the plot #
y = top50['artist'].value_counts()
for i, v in enumerate(y):
    ax.text(v + 0.2, i + .16, str(v), color='black', fontweight='light', fontsize=14)

# export plot as jpg #
plt.savefig('top50_songs_per_artist.jpg', bbox_inches="tight")

popularity = top50['popularity']
artists = top50['artist']

plt.figure(figsize=(10,6))

ax= sb.boxplot(x=popularity, y=artists, data=top50)
plt.xlim(0, 100)
plt.xlabel('Popularity (0-100)')
plt.ylabel('')
plt.title('Song Popularity by Artist', fontweight='bold', fontsize=18)
plt.savefig('top50_artist_popularity.jpg', bbox_inches="tight")
