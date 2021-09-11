#!/usr/bin/env python3

import spotipy

# Normal import
try:
    from redbot.library.tools import load_arguments, load_config
    from redbot.library.spotools import get_user_songs, get_user_playlists
# Allow local import for development purposes
except ModuleNotFoundError:
    from library.tools import load_arguments, load_config
    from library.spotools import get_user_songs, get_user_playlists

def main():
    arguments   = load_arguments()
    config      = load_config("config.ini")
    account     = config["main"]["account"]

    if arguments["account"]:
        account = arguments["account"]

    token = spotipy.util.prompt_for_user_token(
        username        = account,
        scope           = "user-library-read user-library-modify playlist-read-private",
        client_id       = config[account]["id"],
        client_secret   = config[account]["secret"],
        redirect_uri    = 'http://localhost:8888/'
    )

    spotify = spotipy.Spotify(auth=token)

    tracks = get_user_songs(spotify)
    nbbefore = len(tracks)
    albums = dict()
    albums_data = dict()
    toremove = list()
    for item in tracks:
        albums[item['track']['album']['id']] = albums.get(item['track']['album']['id'], 0) + 1
    for id in albums:
        albums_data[id] = spotify.album(id)
    for item in tracks:
        if albums[item['track']['album']['id']] > albums_data[id]['total_tracks'] / 2:
            toremove.append(item['track']["id"])

    print(f"There are {len(toremove)} songs to remove.")
    minilist = list()
    for song in toremove:
        minilist.append(song)
        if len(minilist) >= 20:
            spotify.current_user_saved_tracks_delete(minilist)
            minilist = list()
    tracks = get_user_songs(spotify)

if __name__ == '__main__':
    main()
