#!/usr/bin/env python3

import spotipy

# Normal import
try:
    from redbot.library.tools import load_arguments, load_config
    from redbot.library.spotools import get_liked_songs
# Allow local import for development purposes
except ModuleNotFoundError:
    from library.tools import load_arguments, load_config
    from library.spotools import get_liked_songs

def main():
    arguments   = load_arguments()
    config      = load_config("config.ini")
    account     = config["main"]["account"]

    if arguments["account"]:
        account = arguments["account"]

    token = spotipy.util.prompt_for_user_token(
        username        = account,
        scope           = "user-library-read playlist-read-private",
        client_id       = config[account]["id"],
        client_secret   = config[account]["secret"],
        redirect_uri    = 'http://localhost:8888/'
    )

    spotify = spotipy.Spotify(auth=token)
    # tracks = get_liked_songs(spotify)
    # for item in tracks:
    #     print(f"{item['track']['id']}: {item['track']['name']} by {item['track']['album']['artists'][0]['name']}")

    result = spotify.search("Liked Songs", limit = 50, type = "playlist")
    print(result)


if __name__ == '__main__':
    main()
