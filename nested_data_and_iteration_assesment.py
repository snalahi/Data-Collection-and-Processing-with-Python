# The variable nested contains a nested list. Assign ‘snake’ to the variable output using indexing.

nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]
output = nested[1][2]

# Below, a list of lists is provided. Use in and not in tests to create variables with Boolean values. See comments for further instructions.

lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
if 'yellow' in lst[2]:
    yellow = True
else:
    yellow = False

#Test to see if 4 is in the second list of lst. Save to variable ``four``
if 4 in lst[1]:
    four = True
else:
    four = False

#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
if 'orange' in lst[0]:
    orange = True
else:
    orange = False
    
# Below, we’ve provided a list of lists. Use in statements to create variables with Boolean values - see the ActiveCode window for further directions.

L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
for nest1 in L:
    if 'hola' in nest1:
        test1 = True
    else:
        test1 = False

# Test if [5, 8, 7] is in the list L. Save to variable name test2
if [5, 8, 7] in L:
    test2 = True
else:
    test2 = False

# Test if 6.6 is in the third element of list L. Save to variable name test3
if 6.6 in L[2]:
    test3 = True
else:
    test3 = False
    
# Provided is a nested data structure. Follow the instructions in the comments below. Do not hard code.

nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]],
          'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
data = False
if 'data' in nested.keys():
    data = True

# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
twentyfour = False
if 24 in nested['data']:
    twentyfour = True

# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True,
# otherwise False.

whole = False
if 'whole' not in nested['window']:
    whole = True

# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
physics = False
if 'physics' in nested.keys():
    physics = True
    
# The variable nested_d contains a nested dictionary with the gold medal counts for the top four countries in the past three Olympics. Assign the
# value of Great Britain’s gold medal count from the London Olympics to the variable london_gold. Use indexing. Do not hardcode.

nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22},
            'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
london_gold = nested_d['London']['Great Britain']

# Below, we have provided a nested dictionary. Index into the dictionary to create variables that we have listed in the ActiveCode window.

sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'],
          'diving': ['springboard', 'platform', 'synchronized'],
          'track': ['sprint', 'distance', 'jumps', 'throws'],
          'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'],
                         'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
v1 = sports['swimming'][2]

# Assign the string 'platform' to the name v2
v2 = sports['diving'][1]

# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3 = sports['gymnastics']['women']

# Assign the string 'rings' to the name v4
v4 = sports['gymnastics']['men'][3]

# Given the dictionary, nested_d, save the medal count for the USA from all three Olympics in the dictionary to the list US_count.

nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22},
            'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

US_count = []
for place in nested_d:
    if 'USA' in nested_d[place]:
        US_count.append(nested_d[place]['USA'])
        
# Iterate through the contents of l_of_l and assign the third element of sublist to a new list called third.

l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'],
          ['sea green', 'cornflower', 'lavender', 'indigo'],
          ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]

third = []
for item in l_of_l:
    third.append(item[2])

# Given below is a list of lists of athletes. Create a list, t, that saves only the athlete’s name if it contains the letter “t”. If it does not
# contain the letter “t”, save the athlete name into list other.

athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'],
            ['Felix', 'Bolt', 'Gardner', 'Eaton'],
            ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]

t = []
other = []
for item in athletes:
    for name in item:
        if "t" in name:
            t.append(name)
        else:
            other.append(name)
