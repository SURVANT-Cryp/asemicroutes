#!/Users/patrickquinn/anaconda3/bin/python/
# coding: utf-8

# The open nature of asemic works allows for meaning to occur across linguistic understanding; an asemic text may be “read” in a similar fashion regardless of the reader’s natural language. Multiple meanings for the same symbolism are another possibility for an asemic work, that is, asemic writing can be polysemantic or have zero meaning, infinite meanings, or its meaning can evolve over time.

import string
import random
import googlemaps
import random
import decimal
import textwrap
from random import randint

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

print '\n' + "Suggested Starting Point:" + '\n' + (random_address[0]['formatted_address'])

# Just alphanumeric characters
chars = string.letters + string.digits

# Alphanumeric + special characters
chars = string.letters + string.digits + string.punctuation

routeLength = 10

print('\n' + "Asemic Route:" + '\n' + ''.join((random.choice(chars)) for x in range(routeLength)) + '\n')

