from src.builder import CustomerBuilder
from src.builder import RentalBuilder
from src.builder import MovieBuilder
from src.customer import Customer
from src.movie import Movie
from src.movie import MOVIE_TYPES
from src.movie import TYPE_NEW_RELEASE
from src.movie import TYPE_REGULAR
from src.movie import TYPE_CHILDREN
from src.movie import TYPE_UNKNOWN
from src.rental import Rental

from mock import Mock
import mock
from unittest import TestCase
import unittest

#Copied from the state at the end of chapter 1.

class TestCustomer(TestCase):
    def test_get_name(self):
        self.assertEqual(
                "John",
                CustomerBuilder(name="John").build().name
            )

    def test_no_rentals_statement(self):
        self.assertEqual(
                "Rental record for Jim\n" +
                "Amount owed is 0\n" +
                "You earned 0 frequent renter points",
                CustomerBuilder().build().statement()
                )

    def test_one_new_release_statement(self):
        self.assertEqual(
                "Rental record for Jim\n" +
                "\tNone\n" +
                "Amount owed is 0.0\n" +
                "You earned 0 frequent renter points",
                CustomerBuilder(rental=Mock(spec_set=Rental,
                    **{"get_charge.return_value":0.,
                    "get_points.return_value":0})
                    ).build().statement()
                )

    def test_all_rental_types_statement(self):
        self.assertEqual(
                "Rental record for Pat\n" +
                "\tGodfather 4 9.0\n" +
                "\tScarface 3.5\n" +
                "\tLion King 1.5\n" +
                "Amount owed is 14.0\n" +
                "You earned 4 frequent renter points",
                CustomerBuilder(name="Pat", builders=[
                    RentalBuilder(
                        builder=MovieBuilder(movietype=TYPE_NEW_RELEASE)
                    ),
                    RentalBuilder(
                        builder=MovieBuilder(name="Scarface",
                            movietype=TYPE_REGULAR)
                    ),
                    RentalBuilder(
                        builder=MovieBuilder(name="Lion King",
                            movietype=TYPE_CHILDREN)
                    )]).build().statement()
                )

    def test_new_release_and_regular_statement(self):
        self.assertEqual(
                "Rental record for Steve\n" +
                "\tGodfather 4 9.0\n" +
                "\tScarface 3.5\n" +
                "Amount owed is 12.5\n" +
                "You earned 3 frequent renter points",
                CustomerBuilder(name="Steve", builders=[
                    RentalBuilder(
                        builder=MovieBuilder(movietype=TYPE_NEW_RELEASE)
                    ),
                    RentalBuilder(
                        builder=MovieBuilder(name="Scarface",
                            movietype=TYPE_REGULAR)
                    )
                    ]).build().statement()
                )

    def test_no_rentals_html_statement(self):
        self.assertEqual(
                "<h1>Rental record for <em>David</em></h1>\n" +
                "<p>Amount owed is <em>0</em></p>\n" +
                "<p>You earned <em>0 frequent renter points</em></p>",
                CustomerBuilder(name="David").build().html_statement()
                )

    def test_one_new_release_html_statement(self):
        self.assertEqual(
                "<h1>Rental record for <em>John</em></h1>\n" +
                "<p>Godfather 4 9.0</p>\n" +
                "<p>Amount owed is <em>9.0</em></p>\n" +
                "<p>You earned <em>2 frequent renter points</em></p>",
                CustomerBuilder(name="John", builder=RentalBuilder(
                    builder=MovieBuilder(movietype=TYPE_NEW_RELEASE)
                    )
                    ).build().html_statement()
                )

    def test_all_rental_types_html_statement(self):
        self.assertEqual(
                "<h1>Rental record for <em>Pat</em></h1>\n" +
                "<p>Godfather 4 9.0</p>\n" +
                "<p>Scarface 3.5</p>\n" +
                "<p>Lion King 1.5</p>\n" +
                "<p>Amount owed is <em>14.0</em></p>\n" +
                "<p>You earned <em>4 frequent renter points</em></p>",
                CustomerBuilder(name="Pat", builders=[
                    RentalBuilder(
                        builder=MovieBuilder(movietype=TYPE_NEW_RELEASE)
                    ),
                    RentalBuilder(
                        builder=MovieBuilder(name="Scarface",
                            movietype=TYPE_REGULAR)
                    ),
                    RentalBuilder(
                        builder=MovieBuilder(name="Lion King",
                            movietype=TYPE_CHILDREN)
                    )]).build().html_statement()
                )

    def test_new_release_and_regular_html_statement(self):
        self.assertEqual(
                "<h1>Rental record for <em>Steve</em></h1>\n" +
                "<p>Godfather 4 9.0</p>\n" +
                "<p>Scarface 3.5</p>\n" +
                "<p>Amount owed is <em>12.5</em></p>\n" +
                "<p>You earned <em>3 frequent renter points</em></p>",
                CustomerBuilder(name="Steve", builders=[
                    RentalBuilder(
                        builder=MovieBuilder(movietype=TYPE_NEW_RELEASE)
                    ),
                    RentalBuilder(
                        builder=MovieBuilder(name="Scarface",
                            movietype=TYPE_REGULAR)
                    )
                    ]).build().html_statement()
                )

class TestMovie(TestCase):
    def test_invalid_title(self):
        with self.assertRaises(TypeError):
            MovieBuilder(movietype=TYPE_UNKNOWN).build()

if __name__ == '__main__':
    unittest.main()
