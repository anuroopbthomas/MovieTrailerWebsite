# imports of media.py and fresh_tomatoes.py
import media
import fresh_tomatoes

# instances created from media.py Class Movie
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://tinyurl.com/y8ax3fhq",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://tinyurl.com/ycuej3kt",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
inception = media.Movie("Inception",
                        "Dream layers",
                        "https://tinyurl.com/y8hqdahk",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")
starwars = media.Movie("Star Wars",
                       "A long story about a galaxy far far away",
                       "https://tinyurl.com/y8jdfxae",
                       "https://www.youtube.com/watch?v=1g3_CFmnU7k")
lastjedi = media.Movie("Star Wars: The Last Jedi",
                       "A story about Rey who will learn about the force",
                       "https://tinyurl.com/hmrqd95",
                       "https://www.youtube.com/watch?v=Q0CbN8sfihY")

# List of movie objects
movies = [inception, starwars, lastjedi, toy_story, avatar]

# Call of Fresh Tomatoes Class and function open_movies_page
# with the argument of the list
fresh_tomatoes.open_movies_page(movies)
