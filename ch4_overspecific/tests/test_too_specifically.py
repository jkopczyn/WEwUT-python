from src.builder import CustomerBuilder
from src.customer import Customer
from src.movie  import Movie
from src.rental import Rental

from mock import Mock
import mock
from unittest import TestCase
import unittest

def title_override(title, *args):
    if args[:2] == ("{0} starring {1} {2}", 2):
        return title
    return mock.DEFAULT

class TestCustomer(TestCase):
    def test_recent_rentals_with_2_rentals(self):
        godfather = Mock(spec_set=Movie, **{"get_title.side_effect":
            lambda *x: title_override("Godfather 4", *x) })
        lionking = Mock(spec_set=Movie, **{"get_title.side_effect":
            lambda *x: title_override("Lion King", *x) })
        godfather_rental = Mock(spec_set=Rental, **{"get_movie.side_effect":
            lambda b: godfather if b else DEFAULT})
        lionking_rental = Mock(spec_set=Rental, **{"get_movie.side_effect":
            lambda b: lionking if b else DEFAULT})
        self.assertEqual(
                "Recent rentals:\nGodfather 4\nLion King",
                CustomerBuilder(rentals=[godfather_rental, lionking_rental]
                    ).build().recent_rentals())

    def test_recent_rentals_with_3_rentals(self):
        godfather = Mock(spec_set=Movie, **{"get_title.side_effect":
            lambda *x: title_override("Godfather 4", *x) })
        lionking = Mock(spec_set=Movie, **{"get_title.side_effect":
            lambda *x: title_override("Lion King", *x) })
        mulan = Mock(spec_set=Movie, **{"get_title.side_effect":
            lambda *x: title_override("Mulan", *x) })
        godfather_rental = Mock(spec_set=Rental, **{"get_movie.side_effect":
            lambda b: godfather if b else DEFAULT})
        lionking_rental = Mock(spec_set=Rental, **{"get_movie.side_effect":
            lambda b: lionking if b else DEFAULT})
        mulan_rental = Mock(spec_set=Rental, **{"get_movie.side_effect":
            lambda b: mulan if b else DEFAULT})
        self.assertEqual(
                "Recent rentals:\nGodfather 4\nLion King\nMulan",
                CustomerBuilder(
                    rentals=[godfather_rental, lionking_rental, mulan_rental]
                    ).build().recent_rentals())

    def test_recent_rentals_with_4_rentals(self):
        godfather = Mock(spec_set=Movie, **{"get_title.side_effect":
            lambda *x: title_override("Godfather 4", *x) })
        lionking = Mock(spec_set=Movie, **{"get_title.side_effect":
            lambda *x: title_override("Lion King", *x) })
        mulan = Mock(spec_set=Movie, **{"get_title.side_effect":
            lambda *x: title_override("Mulan", *x) })
        tron = Mock(spec_set=Movie, **{"get_title.side_effect":
            lambda *x: title_override("Tron", *x) })
        godfather_rental = Mock(spec_set=Rental, **{"get_movie.side_effect":
            lambda b: godfather if b else DEFAULT})
        lionking_rental = Mock(spec_set=Rental, **{"get_movie.side_effect":
            lambda b: lionking if b else DEFAULT})
        mulan_rental = Mock(spec_set=Rental, **{"get_movie.side_effect":
            lambda b: mulan if b else DEFAULT})
        tron_rental = Mock(spec_set=Rental, **{"get_movie.side_effect":
            lambda b: tron if b else DEFAULT})
        self.assertEqual(
                "Recent rentals:\nGodfather 4\nLion King\nMulan",
                CustomerBuilder(rentals=[godfather_rental, lionking_rental,
                    mulan_rental, tron_rental]
                    ).build().recent_rentals())
