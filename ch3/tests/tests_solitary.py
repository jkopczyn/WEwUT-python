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

def create_rental_mock(*args, **kwargs):
    attrs = {"get_line_item.return_value": "---",
            "get_charge.return_value": 0.0,
            "get_points.return_value": 0,
            }
    attrs.update(kwargs)
    return Mock(spec_set=Rental, *args, **attrs)


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

    def test_one_rental_statement(self):
        self.assertEqual(
                "Rental record for Jim\n" +
                "\t---\n" +
                "Amount owed is 0.0\n" +
                "You earned 0 frequent renter points",
                CustomerBuilder(rental=create_rental_mock()).build().statement()
                )

    def test_two_rentals_statement(self):
        self.assertEqual(
                "Rental record for Jim\n" +
                "\t---\n\t---\n" +
                "Amount owed is 0.0\n" +
                "You earned 0 frequent renter points",
                CustomerBuilder(rentals=[create_rental_mock(),
                    create_rental_mock()]).build().statement()
                )

    def test_three_rentals_statement(self):
        self.assertEqual(
                "Rental record for Jim\n" +
                "\t---\n\t---\n\t---\n" +
                "Amount owed is 0.0\n" +
                "You earned 0 frequent renter points",
                CustomerBuilder(rentals=[create_rental_mock(),
                    create_rental_mock(), create_rental_mock()
                    ]).build().statement()
                )

    def test_no_rentals_html_statement(self):
        self.assertEqual(
                "<h1>Rental record for <em>Jim</em></h1>\n" +
                "<p>Amount owed is <em>0</em></p>\n" +
                "<p>You earned <em>0 frequent renter points</em></p>",
                CustomerBuilder().build().html_statement()
                )

    def test_one_rental_html_statement(self):
        self.assertEqual(
                "<h1>Rental record for <em>Jim</em></h1>\n" +
                "<p>---</p>\n" +
                "<p>Amount owed is <em>0.0</em></p>\n" +
                "<p>You earned <em>0 frequent renter points</em></p>",
                CustomerBuilder(rental=create_rental_mock()
                    ).build().html_statement()
                )

    def test_two_rentals_html_statement(self):
        self.assertEqual(
                "<h1>Rental record for <em>Jim</em></h1>\n" +
                "<p>---</p>\n<p>---</p>\n" +
                "<p>Amount owed is <em>0.0</em></p>\n" +
                "<p>You earned <em>0 frequent renter points</em></p>",
                CustomerBuilder(rentals=[create_rental_mock(),
                    create_rental_mock()
                    ]).build().html_statement()
                )

    def test_three_rentals_html_statement(self):
        self.assertEqual(
                "<h1>Rental record for <em>Jim</em></h1>\n" +
                "<p>---</p>\n<p>---</p>\n<p>---</p>\n" +
                "<p>Amount owed is <em>0.0</em></p>\n" +
                "<p>You earned <em>0 frequent renter points</em></p>",
                CustomerBuilder(rentals=[create_rental_mock(),
                    create_rental_mock(), create_rental_mock()
                    ]).build().html_statement()
                )

    def test_charge_for_no_rentals(self):
        self.assertEqual(0.0, CustomerBuilder().build().get_total_charge())


    def test_charge_for_two_rentals(self):
        self.assertEqual(
                4.0,
                CustomerBuilder(rentals=[
                    create_rental_mock(**{"get_charge.return_value": 2.0}),
                    create_rental_mock(**{"get_charge.return_value": 2.0})
                    ]).build().get_total_charge()
                )

    def test_charge_for_three_rentals(self):
        self.assertEqual(
                6.0,
                CustomerBuilder(rentals=[
                    create_rental_mock(**{"get_charge.return_value": 2.0}),
                    create_rental_mock(**{"get_charge.return_value": 2.0}),
                    create_rental_mock(**{"get_charge.return_value": 2.0})
                    ]).build().get_total_charge()
                )

    def test_charge_for_two_different_rentals(self):
        self.assertEqual(
                5.2,
                CustomerBuilder(rentals=[
                    create_rental_mock(**{"get_charge.return_value": 2.0}),
                    create_rental_mock(**{"get_charge.return_value": 3.2})
                    ]).build().get_total_charge()
                )

    def test_points_for_no_rentals(self):
        self.assertEqual(0, CustomerBuilder().build().get_total_points())


    def test_points_for_two_rentals(self):
        self.assertEqual(
                4,
                CustomerBuilder(rentals=[
                    create_rental_mock(**{"get_points.return_value": 2}),
                    create_rental_mock(**{"get_points.return_value": 2})
                    ]).build().get_total_points()
                )

    def test_points_for_three_rentals(self):
        self.assertEqual(
                6,
                CustomerBuilder(rentals=[
                    create_rental_mock(**{"get_points.return_value": 2}),
                    create_rental_mock(**{"get_points.return_value": 2}),
                    create_rental_mock(**{"get_points.return_value": 2})
                    ]).build().get_total_points()
                )

    def test_points_for_two_different_rentals(self):
        self.assertEqual(
                3,
                CustomerBuilder(rentals=[
                    create_rental_mock(**{"get_points.return_value": 2}),
                    create_rental_mock(**{"get_points.return_value": 1})
                    ]).build().get_total_points()
                )

class TestMovie(TestCase):
    def test_invalid_title(self):
        with self.assertRaises(TypeError):
            MovieBuilder(movietype=TYPE_UNKNOWN).build()

    def test_charge_for_children_movies(self):
        self.assertEqual(1.5,
                MovieBuilder(movietype=TYPE_CHILDREN).build().get_charge(1))
        self.assertEqual(1.5,
                MovieBuilder(movietype=TYPE_CHILDREN).build().get_charge(2))
        self.assertEqual(1.5,
                MovieBuilder(movietype=TYPE_CHILDREN).build().get_charge(3))
        self.assertEqual(3.0,
                MovieBuilder(movietype=TYPE_CHILDREN).build().get_charge(4))
        self.assertEqual(4.5,
                MovieBuilder(movietype=TYPE_CHILDREN).build().get_charge(5))

    def test_charge_for_new_release_movies(self):
        self.assertEqual(3.0,
                MovieBuilder(movietype=TYPE_NEW_RELEASE).build().get_charge(1))
        self.assertEqual(6.0,
                MovieBuilder(movietype=TYPE_NEW_RELEASE).build().get_charge(2))
        self.assertEqual(9.0,
                MovieBuilder(movietype=TYPE_NEW_RELEASE).build().get_charge(3))
        self.assertEqual(12.0,
                MovieBuilder(movietype=TYPE_NEW_RELEASE).build().get_charge(4))

    def test_charge_for_regular_movies(self):
        self.assertEqual(2.0,
                MovieBuilder(movietype=TYPE_REGULAR).build().get_charge(1))
        self.assertEqual(2.0,
                MovieBuilder(movietype=TYPE_REGULAR).build().get_charge(2))
        self.assertEqual(3.5,
                MovieBuilder(movietype=TYPE_REGULAR).build().get_charge(3))
        self.assertEqual(5.0,
                MovieBuilder(movietype=TYPE_REGULAR).build().get_charge(4))
        self.assertEqual(6.5,
                MovieBuilder(movietype=TYPE_REGULAR).build().get_charge(5))

    def test_points_for_children_movies(self):
        self.assertEqual(1,
                MovieBuilder(movietype=TYPE_CHILDREN).build().get_points(1))
        self.assertEqual(1,
                MovieBuilder(movietype=TYPE_CHILDREN).build().get_points(2))
        self.assertEqual(1,
                MovieBuilder(movietype=TYPE_CHILDREN).build().get_points(3))

    def test_points_for_new_release_movies(self):
        self.assertEqual(1,
                MovieBuilder(movietype=TYPE_NEW_RELEASE).build().get_points(1))
        self.assertEqual(2,
                MovieBuilder(movietype=TYPE_NEW_RELEASE).build().get_points(2))
        self.assertEqual(2,
                MovieBuilder(movietype=TYPE_NEW_RELEASE).build().get_points(3))
        self.assertEqual(2,
                MovieBuilder(movietype=TYPE_NEW_RELEASE).build().get_points(4))

    def test_points_for_regular_movies(self):
        self.assertEqual(1,
                MovieBuilder(movietype=TYPE_REGULAR).build().get_points(1))
        self.assertEqual(1,
                MovieBuilder(movietype=TYPE_REGULAR).build().get_points(2))
        self.assertEqual(1,
                MovieBuilder(movietype=TYPE_REGULAR).build().get_points(3))


if __name__ == '__main__':
    unittest.main()
