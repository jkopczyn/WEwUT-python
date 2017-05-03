from src.builder import CustomerBuilder
from src.customer import Customer
from src.movie  import Movie
from src.rental import Rental

from mock import Mock
import mock
from unittest import TestCase
import unittest

class TestCustomer(TestCase):
    def title_override(title, *args):
        if args[:2] == ["%s starring %s %s", 2]:
            return title
        return DEFAULT

    def recent_rentals_with_2_rentals(self):
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
