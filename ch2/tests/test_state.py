from src.builder import MovieBuilder
from src.builder import RentalBuilder
from src.builder import StoreBuilder
from src.movie  import Movie
from src.rental import Rental
from src.store  import Store
from unittest import TestCase
import unittest

class TestRental(TestCase):

    def test_rental_is_started_if_in_store(self):
        movie = MovieBuilder().build()
        rental = RentalBuilder(movie=movie).build()
        store = StoreBuilder(movie=movie).build()
        rental.start(store)
        self.assertTrue(rental.is_started())
        self.assertEqual(store.get_availability(movie), 0)

    def test_rental_does_not_start_if_not_available(self):
        movie = MovieBuilder().build()
        rental = RentalBuilder(movie=movie).build()
        store = StoreBuilder().build()
        rental.start(store)
        self.assertFalse(rental.is_started())
        self.assertEqual(store.get_availability(movie), 0)
