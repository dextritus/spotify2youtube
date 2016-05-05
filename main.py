from __future__ import print_function
import httplib2
import os
import base64
import codecs

from sendEmail import CreateMessage, SendMessage

from email.mime.text import MIMEText

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

import sys
import spotipy
import spotipy.util as util
from spotify_my_utils import show_tracks
from get_youtube_results import get_youtube_link
from gmail_quick_start import get_credentials

#------------------ SPOTIFY ----------------------------
scope_spotify = 'playlist-modify'
# 'user-library-read'
andreea_pl_id = '2uZLbONDXqEShj7sve6pKu'
andreea_sent_pl_id = '2iMu9IZq9TjvHrzHcXjsY9'


username_spotify = 'dextritus'
song_list = []
song_list2 = " "

def main():
    song_list2 = "<table style='width:600px;table-layout:fixed'>"

    ###### initialize Gmail service
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    gmail_service = discovery.build('gmail', 'v1', http=http)
    ###### 

    ###### initialize Spotify
    token = util.prompt_for_user_token(username_spotify, scope_spotify)

    if token:
        sp = spotipy.Spotify(auth=token)
        playlist = sp.user_playlist(username_spotify, andreea_pl_id, fields = 'tracks')
        playlist2 = sp.user_playlist(username_spotify, andreea_sent_pl_id, fields = 'tracks')
        tracks = playlist['tracks']
        for i, item in enumerate(tracks['items']):
            song = item['track']
            song_id = song['id']
            song_details = str(song['artists'][0]['name'].encode('utf8')) + " " + str(song['name'].encode('utf8'))
            print('-----')
            # song_list.append(song_details+"    ---->   "+get_youtube_link(song_details)+ "<br>")
            song_list2 += "<tr>"
            song_list2 = song_list2 + "<td>"+song_details+"</td>"+"<td>"+get_youtube_link(song_details)+"</td>"
            song_list2 += "</tr>"
            print('-------')

            #remove from andreea playlist, put in andreea_sent playlist
            sp.user_playlist_remove_all_occurrences_of_tracks(username_spotify, andreea_pl_id, [song_id])
            sp.user_playlist_add_tracks(username_spotify, andreea_sent_pl_id, [song_id])

            # print
        if not len(tracks['items']):
            song_list2 = []
    else:
        print('Can''t get token for', username_spotify)
    
    if len(song_list2):
        song_list2 += "</table>"
        message = CreateMessage("popovici.alexandru@gmail.com", "popovici.alexandru@gmail.com", "New Songs", song_list2)
        SendMessage(gmail_service, "me", message)
        # print(song_list2)

if __name__ == '__main__':
    main()