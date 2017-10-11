import media
import fresh_tomatoes
import webbrowser

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys come to life",
                        "http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio",
                        120,
                        "https://en.wikipedia.org/wiki/Toy_Story",
                        100)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     130,
                     "https://en.wikipedia.org/wiki/Avatar_(2009_film)",
                     84)

law_abiding_citzien = media.Movie("Law Abiding Citzien",
                     "An evil geniues who kills everyone while beeing in jail ",
                     "https://images-na.ssl-images-amazon.com/images/I/91P8PtNZzfS._SY445_.jpg",
                     "https://www.youtube.com/watch?v=kMYiObYd9xM",
                     110,
                     "https://en.wikipedia.org/wiki/Law_Abiding_Citizen",
                     26)

game_of_thrones = media.TV_show("Game Of Thrones",
                     "Basically, everyone dies",
                     "http://www.hollywoodreporter.com/sites/default/files/2011/03/got_-_official_poster.jpg",
                     "https://www.youtube.com/watch?v=YinJaXzgzqI",
                     45,
                     "https://de.wikipedia.org/wiki/Game_of_Thrones",
                     7)

arrow = media.TV_show("Arrow",
                     "Rich guy hunts down evil guys with a bow",
                     "https://www.filmempfehlung.com/_bilder/poster/tt2193021_arrow_03.jpg",
                     "https://www.youtube.com/watch?v=ViFb0paKdgg",
                     42,
                     "https://en.wikipedia.org/wiki/Arrow_(TV_series)",
                     5)

lie_to_me = media.TV_show("Lie To Me",
                     "Smart Guy using applied psychology to investigate ",
                     "https://s3.eu-central-1.amazonaws.com/images.serienguide.tv/w680/zg0r8ZjJLC6kun1eGZS0LKvzn8Y.jpg",
                     "https://www.youtube.com/watch?v=tcCo26Ma-oY",
                     45,
                     "https://en.wikipedia.org/wiki/Lie_to_Me",
                     3)

def show_trailer(self):
    """Open up youtube trailer from video instance"""
    webbrowser.open(self.trailer_youtube_url)

# list of movie-instances
movie = [toy_story, avatar, law_abiding_citzien]
# list of tv-instances
tv = [game_of_thrones, arrow, lie_to_me]
print fresh_tomatoes.open_movies_page(movie, tv)
