from builder import CustomerBuilder
from builder import RentalBuilder
from builder import MovieBuilder
from customer import Customer
from movie import Movie
from movie import MOVIE_TYPES
from movie import TYPE_NEW_RELEASE
from movie import TYPE_REGULAR
from movie import TYPE_CHILDREN
from movie import TYPE_UNKNOWN
from rental import Rental

class ObjectMother(object):

    @staticmethod
    def customer_with_one_of_each_rental_type(name):
        cust = ObjectMother.customer_with_one_new_release_and_one_regular(name)
        cust.add_rental(Rental(Movie("Lion King", TYPE_CHILDREN), 3))
        return cust

    @staticmethod
    def customer_with_one_new_release_and_one_regular(name):
        cust = ObjectMother.customer_with_one_new_release(name)
        cust.add_rental(Rental(Movie("Scarface", TYPE_REGULAR), 3))
        return cust

    @staticmethod
    def customer_with_one_new_release(name):
        cust = ObjectMother.customer_with_no_rentals(name)
        cust.add_rental(Rental(Movie("Godfather 4", TYPE_NEW_RELEASE), 3))
        return cust

    @staticmethod
    def customer_with_no_rentals(name):
        return Customer(name)

