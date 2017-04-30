from customer import Customer
from rental import Rental
from movie import Movie
from movie import MOVIE_TYPES
from movie import TYPE_NEW_RELEASE
from movie import TYPE_REGULAR
from movie import TYPE_CHILDREN
from movie import TYPE_UNKNOWN

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

a = CustomerBuilder()
b = a.build()

class RentalBuilder(object):
    def __init__(self, movie=None, days=3, builder=None):
        self.movie = movie
        self.days = days
        if builder and not movie:
            self.movie = builder.build()

    def build(self):
        return Rental(self.movie, self.days)

c = RentalBuilder()
d = c.build()

class MovieBuilder(object):
    def __init__(self, name="Godfather 4", movietype=TYPE_NEW_RELEASE):
        self.name = name
        self.type = movietype

    def build(self):
        return Movie(self.name, self.type)

e = MovieBuilder()
f = e.build()
