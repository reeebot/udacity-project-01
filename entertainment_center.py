#
# entertainment_center.py
#
# main program file
#
# gets latest movie data from themoviedb.org API organized into list (retrieve_movies.py)
# creates media.Movie instances with each movie
# opens website showing all the movie information
#
# media.Movie(title, poster_image_url, trailer_url)
#

import media
import fresh_tomatoes
import retrieve_movies

# gets latest movie data
latest_movies = retrieve_movies.get_movies()

# create instances for each movie
movies = []
for movie in latest_movies:
    movies.append(media.Movie(movie[0],movie[1],movie[2],movie[3]))

# open website with movies
fresh_tomatoes.open_movies_page(movies)
