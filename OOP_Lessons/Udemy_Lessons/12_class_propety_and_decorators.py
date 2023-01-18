# -------------------------------------------------------------------------------------------
# --------------------------- Свойства класса и Свойства Декоратора -------------------------
# -------------------------------------------------------------------------------------------

"""
class MovieRating:
    def __init__(self, rating):
        self.set_rating(rating)
        
    def get_rating(self):
        return self.__rating

    def set_rating(self, value):
        if value < 0:
            raise ValueError("Movie rating cannot be zero")
        self.__rating = value

movie_rating = MovieRating(-10)
"""

class MovieRating:
    def __init__(self, rating):
        self.rating = rating
        
    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value < 0:
            raise ValueError("Movie rating cannot be zero")
        self.__rating = value


movie_rating = MovieRating(-8)
