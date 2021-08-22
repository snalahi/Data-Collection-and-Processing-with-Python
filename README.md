# Data-Collection-and-Processing-with-Python
#### Nested List Phenomenon:
#### [This is the [This is the nested list] outer list]

print([10, 20, 30][1]) => It will create a list of [10, 20, 30] and then print out the 2nd item of that list.

List assignment statement replaces the value at the designated position with the assigned value.

#### JavaScript Object Notation (JSON) is a standard text-based format for representing structured data based on JavaScript object syntax.
It originated with JavaScript. But, Python makes it pretty easy to both read in and write out data in JSON format. In fact, JSON format looks almost exactly like the printout of a Python list or a dictionary. 

#### Dump S => dumps(), dumps an object to a string. Load S => loads(), loads an object from a string in JSON. JSON dot Load S => json.loads(), loads from a string into a Python object either a list or a dictionary, and JSON dot dump S => json.dumps(), dumps from a Python list or dictionary into a string.

#### Understand, Extract, Repeat method of incrementally figuring out how to extract data from a nested data structure.

Mnemonic or specific or related names are good we are working with multiple nested loops.

When we are in control of the data structure is to make it very regular with always the same kinds of items in the same level of nesting. In other words, don't mix integers, lists, and dictionaries as items in a single list.

#### Object1 is Object2 => checks whether Object1 and Object2 are same objects or not. If the objects are same, then their contents will also be same.

#### Object1 == Object2 => checks whether the contents of Object1 and Object2 are same or not. In this case, the objects can be different but their contents can be same or equal.

#### Suppose, to make a deep copy of an original list, create a new list, iterate over the original list and append each item to the new list. Now, the new list will be a deep copy of the original list.

To select all the inner items of a list do this => lst[:], it will take all the inner items of the lst list.

The `map function` makes a new list where each item in the original list is transformed in some way. For example, suppose we want to transform each item by doubling it, so we make a new list that has doubles of all the values in the original list.

#### The key thing in map(transformer function, sequence) and sorted(key-function, sequence) is that, the transformer and key-function is modeled in such a way that the function will be applied to each item of the provided sequence (whatever the transformer or key-function is: named or lambda expression). Finally, the resultant values are accumulated in a new sequence.

#### Map just lets us specify hey, apply this transformer function (triple) to every single item in the sequence (a_list) and return a new list => 
#### new_list = map(triple, a_list)

```
import json
json.dumps(a_sequence, indent=2)
```
#### The above code snippet will provide a prettier look whenever you work with long nested sequence of items.

#### zip() function takes two sequences and zips them together, matching their first items together, their second items together, and so on. It makes it easy to do operations where you have to make pairwise comparisons or pairwise combinations. Provides you the option to match up the items in multiple sequences positionally, so that you can do something with all the first items, something with all the second items, and so on.
#### You can use it (the zip() function) whenever you want to do pairwise operations. For example, if you wanted to take three lists of words and generate a single list that had the longest of the three words in each position, you could first zip all three lists together to generate a list of tuples, then you could write a list comprehension to do a mapping operation, transforming each tuple of three words into a single string, the longest of the three words. 

#### range(5) => 0, 1, 2, 3, 4; Upto but not including the last number.































































