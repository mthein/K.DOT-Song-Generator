from markov_python.cc_markov import MarkovChain

import urllib2

response = urllib2.urlopen('http://www.metrolyrics.com/all-the-stars-lyrics-kendrick-lamar.html')
html = response.read()

print html
