#!/usr/bin/env python3
'''
    These are various tools related to the spotify api used by spotifycleanup
'''

def get_liked_songs(spotify, limit = 50):
    count = limit
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
