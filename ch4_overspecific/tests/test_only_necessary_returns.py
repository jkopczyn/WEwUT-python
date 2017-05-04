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
        godfather = Mock(spec_set=Movie, **{"get_title.return_value": "None"})
        lionking = Mock(spec_set=Movie, **{"get_title.return_value": "None"})
        godfather_rental = Mock(spec_set=Rental, **{"get_movie.side_effect":
            lambda b: godfather if (type(b) == bool) else DEFAULT})
        lionking_rental = Mock(spec_set=Rental, **{"get_movie.side_effect":
            lambda b: lionking if (type(b) == bool) else DEFAULT})
        self.assertEqual(
                "Recent rentals:\nNone\nNone",
                CustomerBuilder(rentals=[godfather_rental, lionking_rental]
                    ).build().recent_rentals())

    def test_recent_rentals_with_3_rentals(self):
        godfather = Mock(spec_set=Movie, **{"get_title.return_value": "None"})
        lionking = Mock(spec_set=Movie, **{"get_title.return_value": "None"})
        mulan = Mock(spec_set=Movie, **{"get_title.return_value": "None"})
        godfather_rental = Mock(spec_set=Rental, **{"get_movie.side_effect":
            lambda b: godfather if (type(b) == bool) else DEFAULT})
        lionking_rental = Mock(spec_set=Rental, **{"get_movie.side_effect":
            lambda b: lionking if (type(b) == bool) else DEFAULT})
        mulan_rental = Mock(spec_set=Rental, **{"get_movie.side_effect":
            lambda b: mulan if (type(b) == bool) else DEFAULT})
        self.assertEqual(
                "Recent rentals:\nNone\nNone\nNone",
                CustomerBuilder(
                    rentals=[godfather_rental, lionking_rental, mulan_rental]
                    ).build().recent_rentals())

    def test_recent_rentals_with_4_rentals(self):
        godfather = Mock(spec_set=Movie, **{"get_title.return_value": "None"})
        lionking = Mock(spec_set=Movie, **{"get_title.return_value": "None"})
        mulan = Mock(spec_set=Movie, **{"get_title.return_value": "None"})
        tron = Mock(spec_set=Movie, **{"get_title.return_value": "None"})
        godfather_rental = Mock(spec_set=Rental, **{"get_movie.side_effect":
            lambda b: godfather if (type(b) == bool) else DEFAULT})
        lionking_rental = Mock(spec_set=Rental, **{"get_movie.side_effect":
            lambda b: lionking if (type(b) == bool) else DEFAULT})
        mulan_rental = Mock(spec_set=Rental, **{"get_movie.side_effect":
            lambda b: mulan if (type(b) == bool) else DEFAULT})
        tron_rental = Mock(spec_set=Rental, **{"get_movie.side_effect":
            lambda b: tron if (type(b) == bool) else DEFAULT})
        self.assertEqual(
                "Recent rentals:\nNone\nNone\nNone",
                CustomerBuilder(rentals=[godfather_rental, lionking_rental,
                    mulan_rental, tron_rental]
                    ).build().recent_rentals())
