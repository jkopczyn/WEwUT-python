from movie import Movie
from movie import MOVIE_TYPES
from movie import TYPE_NEW_RELEASE
from movie import TYPE_REGULAR
from movie import TYPE_CHILDREN
from movie import TYPE_UNKNOWN
from rental import Rental
from store  import Store

class RentalBuilder(object):
    def __init__(self, movie=None, days=3, builder=None):
        self.movie = movie
        self.days = days
        if builder and not movie:
            self.movie = builder.build()

    def build(self):
        return Rental(self.movie, self.days)

class MovieBuilder(object):
    def __init__(self, name="Godfather 4", movietype=TYPE_NEW_RELEASE):
        self.name = name
        self.type = movietype

    def build(self):
        return Movie(self.name, self.type)

class StoreBuilder(object):
    def __init__(self,
            movies=None, movie=None,
            builders=None, builder=None):
        self.movies = movies or []
        if movie:
            self.movies += [movie]
        self.builders = builders or []
        if builder:
            self.builders += [builder]

    def build(self):
        return Store(self.movies + [b.build() for b in self.builders])

