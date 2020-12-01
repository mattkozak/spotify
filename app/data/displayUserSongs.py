#!/usr/bin/env python3

import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from collections import Counter

# load in the data file #
with open("top50_data.txt") as json_file:
    song_data = json.load(json_file)

with open("fav_artists.txt") as json_file:
    artist_data = json.load(json_file)

# initialize empty lists #
list_of_results = song_data[0]["items"]
list_of_artist_names = []
list_of_artist_uri = []
list_of_song_names = []
list_of_song_uri = []
list_of_durations_ms = []
list_of_explicit = []
list_of_albums = []
list_of_popularity = []

# artist data #
list_of_artists = artist_data[0]["items"]
list_of_urls = []
list_of_genres = []
list_of_images = []
list_of_names = []
list_of_artist_popularity = []
list_of_uris = []

for artist in list_of_artists:
    curr_url = artist["external_urls"]["spotify"]
    list_of_urls.append(curr_url)
    curr_genres = artist["genres"]
    for genre in curr_genres:
        list_of_genres.append(genre)
    curr_image = artist["images"][0]["url"]
    list_of_images.append(curr_image)
    curr_name = artist["name"]
    list_of_names.append(curr_name)
    curr_popularity = artist["popularity"]
    list_of_artist_popularity.append(curr_popularity)
    curr_uri = artist["uri"]
    list_of_uris.append(curr_uri)


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

all_artists = pd.DataFrame(
    {'artist': list_of_names,
    'artist_url': list_of_urls,
    'artist_popularity': list_of_artist_popularity,
    'artist_uri': list_of_uris,
    'artist_image' : list_of_images
    })

genres = pd.DataFrame(
    {'genres': list_of_genres
    })

i = 1
category = Counter(list_of_genres)
for value, count in category.most_common(10):
    print(i,") ", value)
    i += 1

# export song list to csv file #
all_songs_saved = all_songs.to_csv('top50_songs.csv')
top50 = all_songs

all_artists_saved = all_artists.to_csv('fav_artists.csv')
genres_saved = genres.to_csv('fav_genres.csv')

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
