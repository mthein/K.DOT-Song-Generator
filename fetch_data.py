import urllib2
from bs4 import BeautifulSoup

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

    
kendrick_lamar = 'http://www.metrolyrics.com/kendrick-lamar-lyrics.html'

kendrick_songs = get_artist_songs(kendrick_lamar)

for link in kendrick_songs:
    get_artist_lyrics(str(link))
