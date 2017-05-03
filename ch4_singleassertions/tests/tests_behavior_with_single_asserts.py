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
    def test_rental_started_if_in_store(self):
        rental = RentalBuilder().build()
        store_mock = Mock(spec_set=Store, **{"get_availability.return_value": 1})
        rental.start(store_mock)
        self.assertTrue(rental.is_started())

    def test_rental_does_not_start_if_not_available(self):
        rental = RentalBuilder().build()
        store_mock = Mock(spec_set=Store, **{"get_availability.return_value": 0})
        rental.start(store_mock)
        self.assertFalse(rental.is_started())

class TestStore(TestCase):
    def test_no_availability_when_empty(self):
        store = StoreBuilder().build()
        self.assertEqual(0, store.get_availability(Mock(spec_set=Movie)))

    def test_available_when_movie_is_stocked(self):
        movie = Mock(spec_set=Movie)
        store = StoreBuilder(movies=[movie,movie]).build()
        self.assertEqual(2, store.get_availability(movie))

    def test_available_when_movie_stocked_and_checked_out(self):
        movie = Mock(spec_set=Movie)
        store = StoreBuilder(movies=[movie,movie]).build()
        store.check_out(movie)
        self.assertEqual(1, store.get_availability(movie))

class TestRentalAndFriends(TestCase):
    def test_store_availability_changes_on_rental(self):
        movie = Mock(spec_set=Movie)
        store = StoreBuilder(movies=[movie,movie]).build()
        rental = RentalBuilder(movie=movie).build()
        rental.start(store)
        RentalBuilder().build().start(store)
        self.assertEqual(1, store.get_availability(movie))
