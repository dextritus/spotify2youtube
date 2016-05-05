import sys
import spotipy
import spotipy.util as util
from spotify_my_utils import show_tracks
from get_youtube_results import get_youtube_link

scope = 'playlist-modify'
andreea_pl_id = '2uZLbONDXqEShj7sve6pKu'
andreea_sent_pl_id = '2iMu9IZq9TjvHrzHcXjsY9'


if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    playlist = sp.user_playlist(username, andreea_pl_id, fields = 'tracks')
    playlist2 = sp.user_playlist(username, andreea_sent_pl_id, fields = 'tracks')
    tracks = playlist['tracks']
    for i, item in enumerate(tracks['items']):
    	song = item['track']
    	song_details = song['artists'][0]['name'] + " " + song['name']
    	print '-------'
    	get_youtube_link(song_details)
    	print '-------'
    	song_id = song['id']
    	print song_id
    	sp.user_playlist_remove_all_occurrences_of_tracks(username, andreea_pl_id, [song_id])
    	sp.user_playlist_add_tracks(username, andreea_sent_pl_id, [song_id])
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