from __future__ import absolute_import
import unittest
from src_refactory.prices import Prices
from src_refactory.main import calculate_price


class MainTests(unittest.TestCase):

    def setUp(self):
        self.prices = Prices()

    def test_can_calculate_small(self):
        brick_price = self.prices.brick_for('4 furos')
        cement_price = self.prices.cement_for('fino')
        for floor in range(1, 4):
            meter_price = calculate_price(floor)
            self.assertEqual(meter_price, cement_price + brick_price)

    def test_can_calculate_medium(self):
        brick_price = self.prices.brick_for('8 furos')
        cement_price = self.prices.cement_for('medio')
        for floor in range(4, 11):
            meter_price = calculate_price(floor)
            self.assertEqual(meter_price, cement_price + brick_price)

    def test_can_calculate_big(self):
        brick_price = self.prices.brick_for('12 furos')
        cement_price = self.prices.cement_for('forte')
        for floor in range(11, 21):
            meter_price = calculate_price(floor)
            self.assertEqual(meter_price, cement_price + brick_price)
