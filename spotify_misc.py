import sys
import spotipy
import spotipy.util as util
from spotify_my_utils import show_tracks
from get_youtube_results import get_youtube_link

scope = 'playlist-modify'
andreea_pl_id = '2uZLbONDXqEShj7sve6pKu'



if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        print playlist['name'], playlist['id']
    
else:
    print "Can't get token for", username

 #    print ' total tracks', playlist['tracks']['total']
	# 	results = sp.user_playlist(username, playlist['id'],
	# 	foields="tracks,next")
	# tracks = results['tracks']
	# show_tracks(tracks)
	# while tracks['next']:
	# 	tracks = sp.next(tracks)
	# 	show_tracks(tracks)