# json.loads() takes a string as input and produces a python object (a dictionary or a list) as output.

import json
a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(a_string)
d = json.loads(a_string)
print("------")
print(type(d))
print(d.keys())
print(d['resultCount'])
# print(a_string['resultCount']) ==> This will produce an error!

### Output of the above block of code: ###
'''
{
 "resultCount":25,
 "results": [
{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}
------
<class 'dict'>
['resultCount', 'results']
25
'''


# json.dumps() takes a python object, typically a dictionary or a list, and returns a string, in JSON format. It has a few other parameters. Two
# useful parameters are sort_keys and indent. When the value True is passed for the sort_keys parameter, the keys of dictionaries are output in
# alphabetic order with their values. The indent parameter expects an integer. When it is provided, dumps generates a string suitable for displaying
# to people, with newlines and indentation for nested lists or dictionaries.

import json
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

print(d)
print('--------')
print(pretty(d))

### Output of the above block of code: ###
'''
{'key1': {'c': True, 'a': 90, '5': 50}, 'key2': {'c': 'yes', 'b': 3}}
--------
{
  "key1": {
    "5": 50,
    "a": 90,
    "c": true
  },
  "key2": {
    "b": 3,
    "c": "yes"
  }
}
