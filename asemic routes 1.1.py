#!/Users/patrickquinn/anaconda3/bin/python/
# coding: utf-8
#   The open nature of asemic works allows for meaning to occur across linguistic understanding; an asemic text may be “read” in a similar fashion regardless of the reader’s natural language. Multiple meanings for the same symbolism are another possibility for an asemic work, that is, asemic writing can be polysemantic or have zero meaning, infinite meanings, or its meaning can evolve over time.

#   “De Quincey describes using the stars to guide him home. Having no knowledge of celestial navigation he finds himself in unfamiliar territories, discovering what he believes are streets anonymous to maps, thus reimagining the city in his own eyes.” (http://www.thedoublenegative.co.uk/2014/12/an-introduction-to-psychogeography/)

import string
import googlemaps
import random
import decimal
import textwrap
import sys
import time
from random import randint
import webbrowser

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(random.random() * 0.1)

gmaps = googlemaps.Client(key='AIzaSyAXmnIhG7oE51Pn9XpD9CZOnz12h1Wl8TA')

top_left=gmaps.reverse_geocode((40.9095863,-73.8919719))
bottom_left=gmaps.reverse_geocode((40.5945483, -74.0584152))
top_right=gmaps.reverse_geocode((40.7924230, -73.7799160))
bottom_right=gmaps.reverse_geocode((40.5894739,-73.7537850))

# get random latitude
rand_lat = float(decimal.Decimal(random.randrange(405945483,409095863))/10000000)

# get random longitude
rand_long = float(decimal.Decimal(random.randrange(-740584152,-737537850))/10000000)

random_address=gmaps.reverse_geocode((rand_lat,rand_long))

print '\n' + "Suggested Direction/Destination:" + '\n' + (random_address[0]['formatted_address'])

# Just alphanumeric characters
chars = string.letters + string.digits

# Alphanumeric + special characters
chars = string.letters + string.digits + string.punctuation

routeLength = 10

slowprint('\n' + "Asemic Route:" + '\n' + ''.join((random.choice(chars)) for x in range(routeLength)) + '\n')

urls = ['https://www.google.com/maps']

for url in urls:
    webbrowser.open_new_tab(url)


