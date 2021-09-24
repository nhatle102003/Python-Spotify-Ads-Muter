import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
from pycaw.pycaw import AudioUtilities


scope = "user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def MuteSpotify(mute):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        if session.Process and session.Process.name() == 'Spotify.exe':
            if mute:
                volume.SetMute(1, None)
                print('Currently Muting Ads')
            else:
                volume.SetMute(0, None)

def main():
    try:
        track_info = sp.current_user_playing_track()
        #print(track_info)

        if track_info['currently_playing_type'] == 'ad':
            MuteSpotify(True)
        else:
            MuteSpotify(False)
            print("Currently playing " + track_info['item']['name'] + " by " + track_info['item']['artists'][0]['name'] + " on Spotify!")

    except:
        print('Nothing is playing right now or something is broken')


while True:
    main()
    time.sleep(0.1)

