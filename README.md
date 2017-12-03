# PROJECT 01 - UDACITY - TIM MEIJOME
udacity project 01 by tim meijome
creates website showing the newest released movies. each movie has a poster, a trailer, and an overview.

## about
retrieve_movies.py
  retrieves information from themoviedb.org API on the 20 newest movies currently in theaters.  creates a formatted list with filtered movie information.

media.py
  movie class constructor.  creates the movie object instances. takes in 4 arguments: title, poster, trailer, overview.

fresh_tomatoes.py
  contains the open_movies_page() function that takes in a list of movie objects and generates the html file website.

entertainment_center.py
  main program.  ties all the scripts together.  sends API request, creates instances of movies with retrieved information, then generates the html file with completed website and opens the file in a new browser tab.

## how to install and run:
to install locally
```
$ git clone https://github.com/reeebot/
```

to run the program
```
$ python entertainment_center.py
```
