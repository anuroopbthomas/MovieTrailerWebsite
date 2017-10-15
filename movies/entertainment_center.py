#imports of media.py and fresh_tomatoes.py
import media
import fresh_tomatoes

#instances created from media.py Class Movie
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
inception = media.Movie("Inception", "Dream layers", "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", "https://www.youtube.com/watch?v=YoHD9XEInc0")
starwars = media.Movie("Star Wars", "A long story about a galaxy far far away", "http://t3.gstatic.com/images?q=tbn:ANd9GcTqRzbG-zvWPx5khd-1D9st1B7FYEq71Gbd2UdaPnrWPwVvY2PX", "https://www.youtube.com/watch?v=1g3_CFmnU7k")
lastjedi = media.Movie("Star Wars: The Last Jedi", "A story about Rey who will learn about the force", "https://upload.wikimedia.org/wikipedia/en/thumb/7/7f/Star_Wars_The_Last_Jedi.jpg/220px-Star_Wars_The_Last_Jedi.jpg", "https://www.youtube.com/watch?v=Q0CbN8sfihY")

#List of movie objects
movies = [inception, starwars, lastjedi, toy_story, avatar]

#Call of Fresh Tomatoes Class and function open_movies_page with the argument of the list
fresh_tomatoes.open_movies_page(movies)
