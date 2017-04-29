from customer import Customer
from movie import Movie
from movie import MOVIE_TYPES
from movie import TYPE_NEW_RELEASE
from movie import TYPE_REGULAR
from movie import TYPE_CHILDREN
from movie import TYPE_UNKNOWN
from rental import Rental
from store  import Store

class CustomerBuilder(object):
    def __init__(self, name="Jim", rentals=None, builders=None, builder=None):
        self.name = name
        if rentals:
            self.rentals = rentals
        elif builders:
            self.rentals = [builder.build() for builder in builders]
        elif builder:
            self.rentals = [builder.build()]
        else:
            self.rentals = []

    def build(self):
        result = Customer(self.name)
        for rental in self.rentals:
            result.add_rental(rental)
        return result

class MovieBuilder(object):
    def __init__(self, name="Godfather 4", movietype=TYPE_NEW_RELEASE):
        self.name = name
        self.type = movietype

    def build(self):
        return Movie(self.name, self.type)

class RentalBuilder(object):
    def __init__(self, movie=None, days=3, builder=None):
        self.movie = movie
        self.days = days
        if builder and not movie:
            self.movie = builder.build()

    def build(self):
        return Rental(self.movie, self.days)

class StoreBuilder(object):
    def __init__(self, movies=[], movie=None, builders=[], builder=None):
        self.movies = movies
        if movie:
            self.movies += [movie]
        self.builders = builders
        if builder:
            self.builders += [builder]

    def build(self):
        return Store(self.movies + [b.build() for b in self.builders])
