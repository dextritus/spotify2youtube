import urllib
import urllib2
from bs4 import BeautifulSoup

def get_youtube_link(textToSearch):
	query = textToSearch.replace(' ', '+')
	print "looking on YouTube for: ", textToSearch
	url = "https://www.youtube.com/results?search_query=" + query
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html,"html.parser")
	for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
	    send_link = '{:60s}'.format('https://www.youtube.com' + vid['href'])
	    print "FOUND! --> "+send_link
	    break

	if not send_link:
		print "sorry, no link found"
		return None

	return send_link