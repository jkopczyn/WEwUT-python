from src.builder import MovieBuilder
from src.movie import Movie
from src.movie import MOVIE_TYPES
from src.movie import TYPE_NEW_RELEASE
from src.movie import TYPE_REGULAR
from src.movie import TYPE_CHILDREN
from src.movie import TYPE_UNKNOWN

from unittest import TestCase
import unittest

class TestMovie(TestCase):
    def test_charge_for_children_1_day(self):
        self.assertEqual(1.5,
                MovieBuilder(movietype=TYPE_CHILDREN).build().get_charge(1))
    def test_charge_for_children_2_day(self):
        self.assertEqual(1.5,
                MovieBuilder(movietype=TYPE_CHILDREN).build().get_charge(2))
    def test_charge_for_children_3_day(self):
        self.assertEqual(1.5,
                MovieBuilder(movietype=TYPE_CHILDREN).build().get_charge(3))
    def test_charge_for_children_4_day(self):
        self.assertEqual(3.0,
                MovieBuilder(movietype=TYPE_CHILDREN).build().get_charge(4))
    def test_charge_for_children_5_day(self):
        self.assertEqual(4.5,
                MovieBuilder(movietype=TYPE_CHILDREN).build().get_charge(5))

    def test_charge_for_new_release_1_day(self):
        self.assertEqual(3.0,
                MovieBuilder(movietype=TYPE_NEW_RELEASE).build().get_charge(1))
    def test_charge_for_new_release_2_day(self):
        self.assertEqual(6.0,
                MovieBuilder(movietype=TYPE_NEW_RELEASE).build().get_charge(2))
    def test_charge_for_new_release_3_day(self):
        self.assertEqual(9.0,
                MovieBuilder(movietype=TYPE_NEW_RELEASE).build().get_charge(3))
    def test_charge_for_new_release_4_day(self):
        self.assertEqual(12.0,
                MovieBuilder(movietype=TYPE_NEW_RELEASE).build().get_charge(4))

    def test_charge_for_regular_1_day(self):
        self.assertEqual(2.0,
                MovieBuilder(movietype=TYPE_REGULAR).build().get_charge(1))
    def test_charge_for_regular_2_day(self):
        self.assertEqual(2.0,
                MovieBuilder(movietype=TYPE_REGULAR).build().get_charge(2))
    def test_charge_for_regular_3_day(self):
        self.assertEqual(3.5,
                MovieBuilder(movietype=TYPE_REGULAR).build().get_charge(3))
    def test_charge_for_regular_4_day(self):
        self.assertEqual(5.0,
                MovieBuilder(movietype=TYPE_REGULAR).build().get_charge(4))
    def test_charge_for_regular_5_day(self):
        self.assertEqual(6.5,
                MovieBuilder(movietype=TYPE_REGULAR).build().get_charge(5))

    def test_points_for_children_1_day(self):
        self.assertEqual(1,
                MovieBuilder(movietype=TYPE_CHILDREN).build().get_points(1))
    def test_points_for_children_2_day(self):
        self.assertEqual(1,
                MovieBuilder(movietype=TYPE_CHILDREN).build().get_points(2))
    def test_points_for_children_3_day(self):
        self.assertEqual(1,
                MovieBuilder(movietype=TYPE_CHILDREN).build().get_points(3))

    def test_points_for_new_release_1_day(self):
        self.assertEqual(1,
                MovieBuilder(movietype=TYPE_NEW_RELEASE).build().get_points(1))
    def test_points_for_new_release_2_day(self):
        self.assertEqual(2,
                MovieBuilder(movietype=TYPE_NEW_RELEASE).build().get_points(2))
    def test_points_for_new_release_3_day(self):
        self.assertEqual(2,
                MovieBuilder(movietype=TYPE_NEW_RELEASE).build().get_points(3))
    def test_points_for_new_release_4_day(self):
        self.assertEqual(2,
                MovieBuilder(movietype=TYPE_NEW_RELEASE).build().get_points(4))

    def test_points_for_regular_1_day(self):
        self.assertEqual(1,
                MovieBuilder(movietype=TYPE_REGULAR).build().get_points(1))
    def test_points_for_regular_2_day(self):
        self.assertEqual(1,
                MovieBuilder(movietype=TYPE_REGULAR).build().get_points(2))
    def test_points_for_regular_3_day(self):
        self.assertEqual(1,
                MovieBuilder(movietype=TYPE_REGULAR).build().get_points(3))
