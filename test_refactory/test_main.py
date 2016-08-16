from __future__ import absolute_import
import unittest
from src_refactory.main import calculate_price


class MainTests(unittest.TestCase):

    def test_can_calculate(self):
        self.assertIsInstance(calculate_price(3), float)
