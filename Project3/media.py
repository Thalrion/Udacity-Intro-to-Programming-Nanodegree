# Parent-Class
class Video():
    '''
    Define __init__ to initialize space in memory for each new instance of the class Video.
    The __init__ function receives the following args:
        self - the name of the object being created
        video_title - contains the title of the video
        video_storyline - contains the storyline of the video
        poster_image - contains url to the poster art for the title
        trailer_youtube - contains the URL for the video trailer
        video_duration - length in minute for the video
        wikipedia_link - contains url to the video
    '''
    def __init__(self, video_title, video_storyline, poster_image, trailer_youtube,
                 video_duration, wikipedia_link):
        self.title = video_title
        self.storyline = video_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.duration = video_duration
        self.wikipedia = wikipedia_link

# Child Class Movie
class Movie(Video):
        '''
        Define __init__ to initialize space in memory for each new instance of the class Movie.
        The __init__ function receives the following args:
            All args inherited from the "Video"-class
            movie_rating - rating taken from https://www.rottentomatoes.com/
        '''
    def __init__(self, video_title, video_storyline, poster_image, trailer_youtube,
                 video_duration, wikipedia_link, movie_rating):
        Video.__init__(self, video_title, video_storyline, poster_image, trailer_youtube,
                     video_duration, wikipedia_link)
        self.ratings = movie_rating

# Child Class Video
class TV_show(Video):
        '''
        Define __init__ to initialize space in memory for each new instance of the class TV_show.
        The __init__ function receives the following args:
            All args inherited from the "Video"-class
            number_of_seasons - number of seasons that were totally aired (not including planned future seasons)
        '''
    def __init__(self, video_title, video_storyline, poster_image, trailer_youtube,
                 video_duration, wikipedia_link, number_of_seasons):
        Video.__init__(self, video_title, video_storyline, poster_image, trailer_youtube,
                     video_duration, wikipedia_link)
        self.seasons = number_of_seasons
