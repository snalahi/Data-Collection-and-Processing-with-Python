When you fetch a web page, the server response where the response code is one of the HTTP headers.  
Errors that you might find while fetching data from a web server:
```
=> '200' means that it was able to respond successfully.
=> '404' means file not found. That is the server doesn't recognize the path that you asked for.
=> '401' means that you're not authorized access to that content,
=> '301' means the content has moved to a different URL.
=> '451' means unavailable for legal reasons. It's intended to be used when resource access is
    denied for legal reasons, like censorship or government mandated blocked access.
```

#### Response objects
Once we run requests.get, a python object is returned. It’s an instance of a class called Response that is defined in the requests module. A Response object, in the full implementation of the `requests module` has the following useful attributes that can be accessed in your program:
```
.text
.url
.json()
.status_code
.headers
.history
```

#### params dictionary substitution in requests.get()
Spaces are substituted as '%20'; multiple key, value pairs are connected with '&' and key to value is represented as key=value in generated URL when requests.get(some_page_url, params=a_dict_should_be_passed) is used to generated URL.

#### To get the actual sense of what the params query would be to extract data from a web server, go for the documentation of that web server!!!!. Mind it!!!

#### params should have a dictionary as it's argument. Two things you should look for. If it's saying that it couldn't generate a valid URL, then either you're not passing in a dictionary or one of the values or keys in the dictionary is not a string.


















