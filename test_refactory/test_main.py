from __future__ import absolute_import
import unittest
from src_refactory.main import calculate_price
from src_refactory.brick import BrickSmall, BrickMedium, BrickBig
from src_refactory.cement import CementTiny, CementMedium, CementStrong


class MainTests(unittest.TestCase):

    def test_can_calculate_small(self):
        brick_price = BrickSmall().price
        cement_price = CementTiny().price

        for floor in range(1, 4):
            meter_price = calculate_price(floor)
            self.assertEqual(meter_price, cement_price + brick_price)

    def test_can_calculate_medium(self):
        brick_price = BrickMedium().price
        cement_price = CementMedium().price

        for floor in range(4, 11):
            meter_price = calculate_price(floor)
            self.assertEqual(meter_price, cement_price + brick_price)

    def test_can_calculate_big(self):
        brick_price = BrickBig().price
        cement_price = CementStrong().price

        for floor in range(11, 31):
            meter_price = calculate_price(floor)
            self.assertEqual(meter_price, cement_price + brick_price)
