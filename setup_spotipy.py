#!/usr/bin/env python3
import spotipy
from spotipy.oauth2 import SpotifyOAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="9c9e13a1069049ceb93c61089e76f066", client_secret= "813b0e982980453e83f66c0782d2ff08", redirect_uri="http://localhost:8888/callback", scope="user-read-private,app-remote-control,user-library-read,user-read-currently-playing,user-read-playback-state,user-modify-playback-state,user-top-read", cache_path = ".spotipy-cache"))
print("Make sure the ssh connection is graphical (-X) and 'chromium-browser' is installed : \n sudo apt update && sudo apt full-upgrade && sudo apt install chromium-browser -y")
print("\n\nAll devices")
for device in sp.devices()["devices"]:
    print(f"{device['name']} : {device['id']}")
