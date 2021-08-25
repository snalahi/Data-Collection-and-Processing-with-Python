# In Python, there’s a module available, called requests. You can use the get function in the requests module to fetch the contents of a page.

import requests
import json

page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
print(type(page)) # this is a Response object from the request class
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched

print("------")
x = page.json() # turn page.text into a python object
# It is something like x = jason.loads(page.text)

print(type(x))
print("---first item in the list---")
print(x[0])
print("---the whole list, pretty printed---")
print(json.dumps(x, indent=2)) # pretty print the results

################ The final print output ##########################
# <class 'requests.Response'>
# [{"word":"money","score":4415,"numSyllables":2},{"word":"honey","score":1206,"numSyllables":2},{"word":"sunny","score":717,"numSyllables":2},{"word":"
# https://api.datamuse.com/words?rel_rhy=funny
# ------
# <class 'list'>
# ---first item in the list---
# {'word': 'money', 'score': 4415, 'numSyllables': 2}
# ---the whole list, pretty printed---
# [{"word":"money","score":4415,"numSyllables":2},{"word":"honey","score":1206,"numSyllables":2},{"word":"sunny","score":717,"numSyllables":2},
# {"word":"bunny","score":702,"numSyllables":2},{"word":"blini","score":613,"numSyllables":2},{"word":"gunny","score":449,"numSyllables":2},
# {"word":"tunny","score":301,"numSyllables":2},{"word":"sonny","score":286,"numSyllables":2},{"word":"dunny","score":245,"numSyllables":2},
# {"word":"runny","score":225,"numSyllables":2},{"word":"thunny","score":222,"numSyllables":2},{"word":"aknee","score":179,"numSyllables":2},
# {"word":"squinny","score":170,"numSyllables":2},{"word":"fiat money","score":160,"numSyllables":4},{"word":"gunnie","score":156,"numSyllables":2},
# {"word":"blood money","score":152,"numSyllables":3},{"word":"squiny","score":151,"numSyllables":2},{"word":"tunney","score":119,"numSyllables":2},
# {"word":"spinny","score":117,"numSyllables":2},{"word":"pin money","score":107,"numSyllables":3},{"word":"easy money","score":66,"numSyllables":4},
# {"word":"smart money","score":66,"numSyllables":3},{"word":"earnest money","score":62,"numSyllables":4},
# {"word":"easter bunny","score":56,"numSyllables":4},{"word":"paper money","score":54,"numSyllables":4},
# {"word":"pocket money","score":47,"numSyllables":4},{"word":"folding money","score":46,"numSyllables":4},
# {"word":"conscience money","score":41,"numSyllables":4},{"word":"hush money","score":40,"numSyllables":3},
# {"word":"prize money","score":37,"numSyllables":3},{"word":"amount of money","score":33,"numSyllables":5},
# {"word":"for love or money","score":32,"numSyllables":5},{"word":"tight money","score":32,"numSyllables":3},
# {"word":"ship money","score":30,"numSyllables":3},{"word":"metal money","score":27,"numSyllables":4},
# {"word":"sum of money","score":23,"numSyllables":4},{"word":"entrance money","score":22,"numSyllables":4},
# {"word":"cheap money","score":21,"numSyllables":3},{"word":"spending money","score":21,"numSyllables":4},
# {"word":"token money","score":21,"numSyllables":4},{"word":"waste of money","score":19,"numSyllables":4},
# {"word":"ransom money","score":18,"numSyllables":4},{"word":"hearth money","score":14,"numSyllables":3},{"word":"munni","score":14,"numSyllables":2},
# {"word":"bunnie","score":2,"numSyllables":2},{"word":"euromoney","score":2,"numSyllables":4},{"word":"smartmoney","score":2,"numSyllables":3},
# {"word":"anyone he","numSyllables":4},{"word":"begun he","numSyllables":3},{"word":"bunney","numSyllables":2},{"word":"ca ne","numSyllables":2},
# {"word":"done he","numSyllables":2},{"word":"donne e","numSyllables":2},{"word":"everyone he","numSyllables":4},{"word":"fun he","numSyllables":2},
# {"word":"grandson he","numSyllables":3},{"word":"gun he","numSyllables":2},{"word":"handgun he","numSyllables":3},{"word":"kun hee","numSyllables":2},
# {"word":"le ne","numSyllables":2},{"word":"lunney","numSyllables":2},{"word":"lunny","numSyllables":2},{"word":"none e","numSyllables":2},
# {"word":"none he","numSyllables":2},{"word":"nun he","numSyllables":2},{"word":"one he","numSyllables":2},{"word":"one knee","numSyllables":2},
# {"word":"pun he","numSyllables":2},{"word":"run e","numSyllables":2},{"word":"run he","numSyllables":2},{"word":"shotgun he","numSyllables":3},
# {"word":"someone e","numSyllables":3},{"word":"someone he","numSyllables":3},{"word":"son e","numSyllables":2},{"word":"son he","numSyllables":2},
# {"word":"sun e","numSyllables":2},{"word":"sun he","numSyllables":2},{"word":"ton he","numSyllables":2},{"word":"ton ne","numSyllables":2},
# {"word":"un e","numSyllables":2},{"word":"un he","numSyllables":2},{"word":"un ne","numSyllables":2},{"word":"un ni","numSyllables":2},
# {"word":"won he","numSyllables":2}]
