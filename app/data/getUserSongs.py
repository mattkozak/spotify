#!/usr/bin/env python3
import os
import sys
import json
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth


# set globals #
PORT_NUMBER = 8080
SPOTIPY_CLIENT_ID = '155f7037499948f9abf0da6fff44787a'
SPOTIPY_CLIENT_SECRET = 'bacdceb31abd43158bcff9064e01d40d'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888'
SCOPE = 'user-top-read'
CACHE = '.spotipyoauthcache'


# set enviromental variables #
os.environ['SPOTIFY_CLIENT_ID'] = SPOTIPY_CLIENT_ID
os.environ['SPOTIFY_CLIENT_SECRET'] = SPOTIPY_CLIENT_SECRET
os.environ['SPOTIFY_REDIRECT_URI'] = SPOTIPY_REDIRECT_URI

# fetch the username #
username = None
token = None
if len(sys.argv) > 1:
    username = sys.argv[1]
    term = sys.argv[2]
    print("Howdy,", username, " lets blow this popsicle stand")
else:
    print("Usage: %s username duration" % (sys.argv[0],))
    print("      username: your Spotify username")
    print("      duration: short_term, medium_term, or long_term")
    sys.exit()

# initiate request for specific username #
#client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)

#sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE, username=username, cache_path=CACHE))
#sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE, cache_path=CACHE))

#token = util.prompt_for_user_token(username, SCOPE, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)

try:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, SCOPE, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)
except:
    token = util.prompt_for_user_token(username, SCOPE, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)

#sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE, username=username))
sp = spotipy.Spotify(auth=token)
user = sp.current_user()
displayname = user["display_name"]
print("Hello, ", displayname)

# check that request was successful and export user data as a .json file #
if token:
    sp = spotipy.Spotify(auth=token)
    song_results = sp.current_user_top_tracks(limit=50, offset=0, time_range=term)
    artist_results = sp.current_user_top_artists(limit=50, offset=0, time_range=term)
    print("Exporting", username, "listening trends to .json file...")
    for song in range(50):
        song_list = []
        song_list.append(song_results)
        with open('top50_data.txt', 'w', encoding='utf-8') as f:
            json.dump(song_list, f, ensure_ascii=False, indent=4)
    for artist in range(50):
        artist_list = []
        artist_list.append(artist_results)
        with open('fav_artists.txt', 'w', encoding='utf-8') as f2:
            json.dump(artist_list, f2, ensure_ascii=False, indent=4)
    print("Complete. Please run ./displayUserSongs.py to generate visuals")

else:
    print("Cannot get token for", username, ". Please try again")

