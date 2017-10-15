#import of module webbrowser
import webbrowser

#class Movie is being made here in media.py
class Movie():
    #documentation of class
    """ This class provides a way to store movie related information

        Attributes:
            title: the string movie title for any given instance
            storyline: the string storyline for any given isntance
            poster_image_url: the string that contains the url for the image of the movie's poster_image_url
            trailer_youtube_url: the string that contains the url for the YouTube link of movie trailer
    """

    #Class variables
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    #Initial constructor function that is called with a new instance is created
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        #Instance Variables
        """Inits Movie with title, storyline, poster_image_url, and trailer_youtube_url        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    #Function that will open webbrowser with the movie's trailer
    def show_trailer(self):
        """Performs the action of opening the webbrowser with the youtube trailer link"""
        webbrowser.open(self.trailer_youtube_url)
