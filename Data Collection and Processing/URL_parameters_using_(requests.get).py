# Here’s an executable sample, using the optional params parameter of requests.get. It gets the same data from the datamus api that we saw previously.
# Here, however, the full url is built inside the call to requests.get

import requests

# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
kval_pairs = {'rel_rhy': 'funny'}
page = requests.get("https://api.datamuse.com/words", params=kval_pairs)
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched

############## The actual output ##########################
# [{"word":"money","score":4415,"numSyllables":2},{"word":"honey","score":1206,"numSyllables":2},{"word":"sunny","score":717,"numSyllables":2},
# {"word":"
# https://api.datamuse.com/words?rel_rhy=funny
