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
from object_mother import ObjectMother
from rental import Rental
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
        pass

    def exp_statement(self, format_string, customer, rental_info):
        pass

    def test_get_name(self):
        self.assertEqual(self.david_name, self.david.get_name())
        self.assertEqual(self.john_name,  self.john.get_name())
        self.assertEqual(self.pat_name,   self.pat.get_name())
        self.assertEqual(self.steve_name, self.steve.get_name())

    def test_statement(self):
        for c in self.customers:
            self.assertEqual(
                    self.exp_statement("Rental record for {0}" +
                        "{1}Amount owed is {2}\n" +
                        "You earned {3} frequent renter points",
                        c,
                        self.rental_info("\t", "", c.get_rentals())),
                    c.statement())

    def test_html_statement(self):
        assert False

    def test_invalid_title(self):
        with self.assertRaises(ArgumentError):
            pass


if __name__ == '__main__':
    unittest.main()
