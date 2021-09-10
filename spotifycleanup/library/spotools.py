#!/usr/bin/env python3
'''
    These are various tools related to the spotify api used by spotifycleanup
'''

def get_user_songs(spotify, limit = 50):
    results = spotify.current_user_saved_tracks(limit=limit)
    tracks  = results['items']
    print(len(tracks))
    while results["next"]:
        tracks.extend(spotify.next(results)['items'])
        print(len(tracks))
        if len(tracks) > 2300:
            break

    print(f"Found {len(tracks)} results")
    return tracks

def get_user_playlists(spotify, limit = 50):
    results     = spotify.current_user_playlists(limit=limit)
    playlists   = results['items']
    print(len(playlists))
    while results["next"]:
        playlists.extend(spotify.next(results)['items'])
        print(len(playlists))
        if len(playlists) > 150:
            break

    print(f"Found {len(playlists)} results")
    return playlists
