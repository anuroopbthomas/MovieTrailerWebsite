#import of module webbrowser
import webbrowser

#class Movie is being made here in media.py
class Movie():
    #documentation of class
    """ This class provides a way to store movie related information"""

    #Class variables
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    #Initial function that is called with a new instance is created
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        #Instance Variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    #Function that will open webbrowser with the movie's trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
