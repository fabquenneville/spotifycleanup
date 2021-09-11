#!/usr/bin/env python3
'''
    These are various tools related to the spotify api used by spotifycleanup
'''

def get_user_songs(spotify, limit = 50, cap = 5000, verbose = False):
    results = spotify.current_user_saved_tracks(limit=limit)
    tracks  = results['items']
    if verbose:
        print(len(tracks))
    while results["next"] and len(tracks) < cap:
        results = spotify.next(results)
        tracks.extend(results['items'])
        if verbose:
            print(len(tracks))

    print(f"Found {len(tracks)} songs.")
    return tracks

def get_user_playlists(spotify, limit = 50, cap = 150, verbose = False):
    results     = spotify.current_user_playlists(limit=limit)
    playlists   = results['items']
    if verbose:
        print(len(playlists))
    while results["next"] and len(playlists) < cap:
        playlists.extend(spotify.next(results)['items'])
        if verbose:
            print(len(playlists))

    print(f"Found {len(playlists)} playlists.")
    return playlists
