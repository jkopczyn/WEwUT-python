from src.builder import CustomerBuilder
from src.customer import Customer
from src.movie  import Movie
from src.rental import Rental

from mock import Mock
import mock
from unittest import TestCase
import unittest

class TestCustomer(TestCase):
    def test_recent_rentals_with_2_rentals(self):
        movie_mock = Mock(spec_set=Movie, **{"get_title.return_value": "None"})
        rental_mock = Mock(spec_set=Rental, **{"get_movie.side_effect":
            lambda b: movie_mock if (type(b) == bool) else DEFAULT})
        self.assertEqual(
                "Recent rentals:\nNone\nNone",
                CustomerBuilder(rentals=[rental_mock, rental_mock]
                    ).build().recent_rentals())

    def test_recent_rentals_with_3_rentals(self):
        movie_mock = Mock(spec_set=Movie, **{"get_title.return_value": "None"})
        rental_mock = Mock(spec_set=Rental, **{"get_movie.side_effect":
            lambda b: movie_mock if (type(b) == bool) else DEFAULT})
        self.assertEqual(
                "Recent rentals:\nNone\nNone\nNone",
                CustomerBuilder(rentals=[rental_mock, rental_mock, rental_mock]
                    ).build().recent_rentals())

    def test_recent_rentals_with_4_rentals(self):
        movie_mock = Mock(spec_set=Movie, **{"get_title.return_value": "None"})
        rental_mock = Mock(spec_set=Rental, **{"get_movie.side_effect":
            lambda b: movie_mock if (type(b) == bool) else DEFAULT})
        self.assertEqual(
                "Recent rentals:\nNone\nNone\nNone",
                CustomerBuilder(rentals=[rental_mock, rental_mock,
                    rental_mock, rental_mock]
                    ).build().recent_rentals())
