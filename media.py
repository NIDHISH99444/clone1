import webbrowser
class Movie :
    """This class stores movie related information"""
    VALID_RATING=["G","PG","R"]
    def __init__(udacity,movieTitle,movieStoryLine,posterImage,youtubeTrailer):
        udacity.title=movieTitle
        udacity.storyline=movieStoryLine
        udacity.poster_image_url=posterImage
        udacity.trailer_youtube_url=youtubeTrailer
        print("Done my job......")

    def showTrailer(self):
        webbrowser.open(self.traileryoutube)