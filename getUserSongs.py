#!/usr/bin/env python3

import os
import sys
import json
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

# globals #
PORT_NUMBER = 8080
SPOTIPY_CLIENT_ID = '155f7037499948f9abf0da6fff44787a'
SPOTIPY_CLIENT_SECRET = 'bacdceb31abd43158bcff9064e01d40d'
SPOTIPY_REDIRECT_URI = 'http://localhost:8080/callback'
SCOPE = 'user-top-read'
CACHE = '.spotipyoauthcache'

# create enviromental variables #
os.environ['SPOTIFY_CLIENT_ID'] = SPOTIPY_CLIENT_ID
os.environ['SPOTIFY_CLIENT_SECRET'] = SPOTIPY_CLIENT_SECRET
os.environ['SPOTIFY_REDIRECT_URI'] = SPOTIPY_REDIRECT_URI

# get the username #
username = ""
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

# initiate request for specific username #
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

token = util.prompt_for_user_token(username, SCOPE, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)

# check that request was successful #
if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Cannot get token for ", username)

# export data as a json #
if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_top_tracks(limit=50, offset=0, time_range='medium_term')
    for song in range(50):
        list = []
        list.append(results)
        with open('top50_data.txt', 'w', encoding='utf-8') as f:
            json.dump(list, f, ensure_ascii=False, indent=4)
    else:
        print("Cannot get token for", username)
