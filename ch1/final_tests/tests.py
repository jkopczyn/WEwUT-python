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
from unittest import TestCase
import unittest

class TestCustomer(TestCase):
    def test_get_name(self):
        self.assertEqual(
                "John",
                CustomerBuilder(name="John").build().name
            )

    def test_no_rentals_statement(self):
        self.assertEqual(
                "Rental record for David\n" +
                "Amount owed is 0.0\n" +
                "You earned 0 frequent renter points",
                CustomerBuilder(name="David").build().statement()
                )

    def test_one_new_release_statement(self):
        self.assertEqual(
                "Rental record for John\n" +
                "\tGodfather 4 9.0\n" +
                "Amount owed is 9.0\n" +
                "You earned 2 frequent renter points",
                CustomerBuilder(name="John", builder=RentalBuilder(
                    builder=MovieBuilder(movietype=TYPE_NEW_RELEASE)
                    )
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
