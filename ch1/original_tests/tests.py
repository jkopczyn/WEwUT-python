from src.customer import Customer
from src.movie import Movie
from src.movie import MOVIE_TYPES
from src.movie import TYPE_NEW_RELEASE
from src.movie import TYPE_REGULAR
from src.movie import TYPE_CHILDREN
from src.movie import TYPE_UNKNOWN
from src.object_mother import ObjectMother
from src.rental import Rental
from unittest import TestCase
import unittest

class TestCustomer(TestCase):
    def setUp(self):
        self.david_name = "David"
        self.john_name = "John"
        self.pat_name = "Pat"
        self.steve_name = "Steve"
        self.david = ObjectMother.customer_with_no_rentals(self.david_name)
        self.john = ObjectMother.customer_with_one_new_release(self.john_name)
        self.pat = ObjectMother.customer_with_one_of_each_rental_type(
                self.pat_name)
        self.steve = ObjectMother.customer_with_one_new_release_and_one_regular(
                self.steve_name)
        self.customers = [self.david, self.john, self.pat, self.steve]

    def rental_info(self, starts_with, ends_with, rentals):
        result = ""
        for rental in rentals:
            result +="{0}{1} {2}{3}\n".format(
                    starts_with,
                    rental.movie.get_title(),
                    rental.get_charge(),
                    ends_with)
        return result

    def exp_statement(self, format_string, customer, rental_info):
        return format_string.format(customer.name, rental_info,
                customer.get_total_charge(), customer.get_total_points())

    def test_get_name(self):
        self.assertEqual(self.david_name, self.david.name)
        self.assertEqual(self.john_name,  self.john.name)
        self.assertEqual(self.pat_name,   self.pat.name)
        self.assertEqual(self.steve_name, self.steve.name)

    def test_statement(self):
        for c in self.customers:
            self.assertEqual(
                    self.exp_statement("Rental record for {0}\n" +
                        "{1}Amount owed is {2}\n" +
                        "You earned {3} frequent renter points",
                        c,
                        self.rental_info("\t", "", c.get_rentals())),
                    c.statement())

    def test_html_statement(self):
        for c in self.customers:
            self.assertEqual(
                    self.exp_statement(
                        "<h1>Rental record for <em>{0}</em></h1>\n{1}" +
                        "<p>Amount owed is <em>{2}</em></p>\n" +
                        "<p>You earned <em>{3} frequent renter points</em></p>",
                        c,
                        self.rental_info("<p>", "</p>", c.get_rentals())),
                    c.html_statement())

    def test_invalid_title(self):
        with self.assertRaises(TypeError):
            ObjectMother.customer_with_no_rentals("Bob").add_rental(
                    Rental(Movie("Crazy, Stupid, Love.", TYPE_UNKNOWN), 4))


if __name__ == '__main__':
    unittest.main()
