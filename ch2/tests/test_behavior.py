from src.builder import MovieBuilder
from src.builder import RentalBuilder
from src.builder import StoreBuilder
from src.movie  import Movie
from src.rental import Rental
from src.store  import Store

from mock import Mock
import mock
from unittest import TestCase
import unittest

class TestRental(TestCase):

    def test_rental_is_started_if_in_store(self):
        movie = MovieBuilder().build()
        rental = RentalBuilder(movie=movie).build()
        store = Mock(spec_set=Store)
        store.configure_mock(**{'get_availability.return_value': 1})
        rental.start(store)
        self.assertTrue(rental.is_started())
        store.check_out.assert_called_with(movie)
        pass

    def test_rental_does_not_start_if_not_available(self):
        movie = MovieBuilder().build()
        rental = RentalBuilder(movie=movie).build()
        pass

if __name__ == '__main__':
    unittest.main()
