from src.builder import RentalBuilder
from src.movie  import Movie
from src.rental import Rental
from src.store  import Store

from mock import Mock
import mock
from unittest import TestCase
import unittest

class TestRental(TestCase):
    def test_rental_started_if_in_store(self):
        movie_mock = Mock(spec_set=Movie)
        rental = RentalBuilder(movie=movie_mock).build()
        store_mock = Mock(spec_set=Store, **{"get_availability.return_value": 1})
        rental.start(store_mock)
        self.assertTrue(rental.is_started())
        store_mock.check_out.assert_called_with(movie_mock)

    def test_rental_does_not_start_if_not_available(self):
        movie_mock = Mock(spec_set=Movie)
        rental = RentalBuilder(movie=movie_mock).build()
        store_mock = Mock(spec_set=Store, **{"get_availability.return_value": 0})
        rental.start(store_mock)
        self.assertFalse(rental.is_started())
        store_mock.check_out.assert_not_called()
