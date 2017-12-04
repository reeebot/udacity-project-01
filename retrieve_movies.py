#
# retrieve_movies.py
#
# function that retrieves movie information from themoviedb.org API
#


import httplib
import json


def get_movies():
    # set domain for GET
    conn = httplib.HTTPSConnection("api.themoviedb.org")
    payload = "{}"
    # GET request to themoviedb.org API
    conn.request(
        "GET", "/3/discover/movie?page=1&include_video=false&include_adult=" +
        "false&sort_by=popularity.desc&language=en-US&api_key=" +
        "776ecd6d5ef23c833c92236e4297d694", payload)
    res = conn.getresponse()
    # puts GET response into 'data' variable
    data = {}
    data = res.read()
    # convert data to JSON
    data_json = json.loads(data)
    # filter only the results
    results = data_json["results"]
    # empty list for movie information
    latest_movies = []

    # for each movie in the results:
    for movie in results:
        # GET trailer video information
        conn.request(
            "GET", "/3/movie/"+str(movie["id"]) +
            "/videos?api_key=776ecd6d5ef23c833c92236e4297d694", payload)
        res = conn.getresponse()
        video_data = {}
        video_data = res.read()
        video_data_json = json.loads(video_data)
        # add the title/poster_path/video_url of each movie to latest_movies
        movie_info = [str(movie["title"]), "https://image.tmdb.org/t/p/w500" +
                      str(movie["poster_path"]),
                      "https://www.youtube.com/watch?v=" +
                      str(video_data_json["results"][0]["key"]),
                      movie["overview"].encode('utf-8')]
        latest_movies.append(movie_info)

    # returns a list with all movie information formatted
    return latest_movies
