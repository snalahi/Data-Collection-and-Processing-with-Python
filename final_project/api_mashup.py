import requests_with_caching
import json

# Your first task will be to fetch data from TasteDive. The documentation for the API is at https://tastedive.com/read/api.
# Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the name of a movie or music artist.
# The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, not other kinds of media.
# It will be a python dictionary with just one key, ‘Similar’.
# Try invoking your function with the input “Black Panther”.

# HINT: Be sure to include only q, type, and limit as parameters in order to extract data from the cache. If any other parameters are included,
# then the function will not be able to recognize the data that you’re attempting to pull from the cache. Remember, you will not need an api key
# in order to complete the project, because all data will be found in the cache.

def get_movies_from_tastedive(name): 
    base_url = 'https://tastedive.com/api/similar'
    parameters = {'q':name, 'type':'movies', 'limit':5}
    result = requests_with_caching.get(base_url, params=parameters)
    return json.loads(result.text)

# You will need to write a function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive.
# Call it extract_movie_titles.
  
def extract_movie_titles(movie_dict):
    return [i['Name'] for i in movie_dict['Similar']['Results']]

# You’ll write a function, called get_related_titles. It takes a list of movie titles as input. It gets five related movies for each from
# TasteDive, extracts the titles for all of them, and combines them all into a single list. Don’t include the same movie twice.
  
def get_related_titles(title_lst):
    result_lst = []
    for i in title_lst:
        for j in get_movies_from_tastedive(i)['Similar']['Results']:
            if j['Name'] not in result_lst:
                result_lst.append(j['Name'])
    return result_lst

# Your next task will be to fetch data from OMDB. The documentation for the API is at https://www.omdbapi.com/
# Define a function called get_movie_data. It takes in one parameter which is a string that should represent the title of a movie you want to
# search. The function should return a dictionary with information about that movie.
# Again, use requests_with_caching.get(). For the queries on movies that are already in the cache, you won’t need an api key. You will need to
# provide the following keys: t and r. As with the TasteDive cache, be sure to only include those two parameters in order to extract existing
# data from the cache.  
  
def get_movie_data(title):
    base_url = 'http://www.omdbapi.com/'
    parameters = {'t':title, 'r':'json'}
    result = requests_with_caching.get(base_url, params=parameters)
    return json.loads(result.text)

# Now write a function called get_movie_rating. It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an
# integer. For example, if given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.  
  
def get_movie_rating(movie_dict):
    # Since the 2nd item in the Ratings dictionary is related to Rotten Tomatoes
    # Actually Source:Rotten Tomatoes
    if (1 < len(movie_dict['Ratings'])) and ('Rotten Tomatoes' in movie_dict['Ratings'][1].values()):
        return int(movie_dict['Ratings'][1]['Value'].replace('%', ''))
    else:
        return 0

# Now, you’ll put it all together. Define a function get_sorted_recommendations. It takes a list of movie titles as an input. It returns a sorted
# list of related movie titles as output, up to five related movies for each input movie title. The movies should be sorted in descending order by
# their Rotten Tomatoes rating, as returned by the get_movie_rating function. Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes
# before ‘Eyyvah Eyvah’.     
      
def get_sorted_recommendations(title_lst):
    result_dict = {}
    movie_lst = get_related_titles(title_lst)
    for i in movie_lst:
        result_dict[i] = get_movie_rating(get_movie_data(i))
    return [j[0] for j in sorted(result_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)]

get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])


#### Some realizations on code line 71 ######
result = {'Baby Mama': 64, 'The Five-Year Engagement': 63, 'Bachelorette': 56, 'The Heat': 65,
          'Date Night': 67, 'Sherlock Holmes: A Game Of Shadows': 60, 'Yahşi Batı': 0, 'Eyyvah Eyvah': 0,
          'Pirates Of The Caribbean: On Stranger Tides': 32, 'Prince Of Persia: The Sands Of Time': 36}

# So, the key function or the lambda expression is expressing that firstly, the tuples will get sorted on the
# basis of ratings and then if two ratings are similar than it will go for the names and as stated it will order
# those in reverse alphabetic order.
lst = [i[0] for i in sorted(result.items(), key=lambda x: (x[1], x[0]), reverse=True)]

print(result)
print()
print(lst)

###################### Output ##############################
# {'Baby Mama': 64, 'The Five-Year Engagement': 63, 'Bachelorette': 56, 'The Heat': 65, 'Date Night': 67, 'Sherlock Holmes: A Game Of Shadows': 60,
# 'Yahşi Batı': 0, 'Eyyvah Eyvah': 0, 'Pirates Of The Caribbean: On Stranger Tides': 32, 'Prince Of Persia: The Sands Of Time': 36}

# ['Date Night', 'The Heat', 'Baby Mama', 'The Five-Year Engagement', 'Sherlock Holmes: A Game Of Shadows', 'Bachelorette',
# 'Prince Of Persia: The Sands Of Time', 'Pirates Of The Caribbean: On Stranger Tides', 'Yahşi Batı', 'Eyyvah Eyvah']
