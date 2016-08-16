from __future__ import absolute_import
import unittest
from src_refactory.prices import Prices


class PricesTests(unittest.TestCase):

    def setUp(self):
        self.prices = Prices()

    def test_price_attributes(self):
        self.assertIsInstance(self.prices.cements, dict)
        self.assertIsInstance(self.prices.bricks, dict)

    def test_price_for_cement(self):
        for name, price in self.prices.cements.items():
            self.assertEqual(self.prices.cement_for(name), price)

    def test_price_for_brick(self):
        for name, price in self.prices.bricks.items():
            self.assertEqual(self.prices.brick_for(name), price)
