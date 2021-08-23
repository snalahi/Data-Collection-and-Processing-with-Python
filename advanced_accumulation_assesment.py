# Write code to assign to the variable map_testing all the elements in lst_check while adding the string “Fruit: ” to the beginning of each element
# using mapping.

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
map_testing = map(lambda x: "Fruit: " + x, lst_check)

# Below, we have provided a list of strings called countries. Use filter to produce a list called b_countries that only contains the strings from
# countries that begin with B.

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh',
             'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
b_countries = filter(lambda x: x[0] == 'B', countries)

# Below, we have provided a list of tuples that contain the names of Game of Thrones characters. Using list comprehension, create a list of strings
# called first_names that contains only the first names of everyone in the original list.

people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'),
          ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'),
          ('Baelish', 'Peter')]
first_names = [name[1] for name in people]

# Use list comprehension to create a list called lst2 that doubles each element in the list, lst.

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
lst2 = [element * 2 for element in lst]

# Below, we have provided a list of tuples that contain students’ names and their final grades in PYTHON 101. Using list comprehension, create a new
# list passed that contains the names of students who passed the class (had a final grade of 70 or greater).

students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]
passed = [student[0] for student in students if student[1] >= 70]

# Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to the variable opposites if they are
# both longer than 3 characters each.

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
opposites = filter(lambda x: len(x[0]) >= 3 and len(x[1]) >= 3, zip(l1, l2))

# Below, we have provided a species list and a population list. Use zip to combine these lists into one list of tuples called pop_info. From this
# list, create a new list called endangered that contains the names of species whose populations are below 2500.

species = ['golden retriever', 'white tailed deer', 'black rhino',
           'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant',
           'rainbow trout', 'black bear', 'blue whale', 'water moccasin',
           'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300,
              7500, 100, 1800, 9500, 125000]

pop_info = zip(species, population)
endangered = [item[0] for item in pop_info if item[1] < 2500]
