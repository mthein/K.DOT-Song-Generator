import urllib2
import os
from bs4 import BeautifulSoup

#
def html_maker(website):
    links = urllib2.urlopen(website)
    return links.read()

def get_artist_songs(links):
    html = html_maker(links)
    soup = BeautifulSoup(html, 'html.parser')

    new_links = soup.find_all('a', 'title')

    artist_songs = []

    for link in new_links:
        artist_songs.append(link.get('href'))

    return artist_songs

def get_artist_lyrics(links):
    html = html_maker(links)
    soup = BeautifulSoup(html, 'html.parser')

    lyrics = soup.find_all('p', 'verse')

    lyrics_soup = BeautifulSoup(str(lyrics), 'html.parser')

    f = open("phrase_bank.txt", "a+")
    f.write (((lyrics_soup.get_text()).replace('\\n', '\n')) + ('\n'))

# Artist we will be generating songs in the style of:
kendrick_lamar = 'http://www.metrolyrics.com/kendrick-lamar-lyrics.html'


kendrick_songs = get_artist_songs(kendrick_lamar)

if os.path.isfile("phrase_bank.txt"):
    os.remove("phrase_bank.txt")
else:    # Show an error
    print("Error: phrase_bank.txt file not found")

for link in kendrick_songs:
    get_artist_lyrics(str(link))
