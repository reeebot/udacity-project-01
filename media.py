#
# media.py
#
# class defining "movie" constructor
#

class Movie():
    def __init__(self, title, poster_url, trailer_url, overview):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url
        self.overview = overview
