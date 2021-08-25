# Suppose you were writing a computer program that was going to automatically translate paragraphs of text into paragraphs with similar meanings but
# with more rhymes. You would want to contact the datamuse API repeatedly, passing different values associated with the key rel_rhy. Let’s make a
# python function to do that. You can think of it as a wrapper for the call to requests.get.

import requests

def get_rhymes(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["rel_rhy"] = word
    params_diction["max"] = "3" # get at most 3 results
    resp = requests.get(baseurl, params=params_diction)
    # return the top three words
    word_ds = resp.json()
    return [d['word'] for d in word_ds]
    # This actually doesn't run when the above line is returned
    return resp.json() # Return a python object (a list of dictionaries in this case)

print(get_rhymes("funny"))
print(get_rhymes("dash"))

################### The output #################################
# ['money', 'honey', 'sunny']
# ['cache', 'flash', 'ash']
