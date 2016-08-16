from __future__ import absolute_import
import unittest
from src_refactory.construction import Construction
from src_refactory.prices import Prices


class ConstructionTests(unittest.TestCase):

    def test_construction_attributes(self):
        construction = Construction(3)
        self.assertIsInstance(construction.floors, int)
        self.assertIsInstance(construction.cement, str)
        self.assertIsInstance(construction.brick, str)

    def test_construction_one_to_three_floors(self):
        cement = 'fino'
        brick = '4 furos'
        for floors in range(1, 4):
            construction = Construction(floors)
            self.assertEqual(cement, construction.cement)
            self.assertEqual(brick, construction.brick)

    def test_construction_four_to_ten_floors(self):
        cement = 'medio'
        brick = '8 furos'
        for floors in range(4, 11):
            construction = Construction(floors)
            self.assertEqual(cement, construction.cement)
            self.assertEqual(brick, construction.brick)

    def test_construction_more_than_ten(self):
        cement = 'forte'
        brick = '12 furos'
        for floors in range(11, 20):
            construction = Construction(floors)
            self.assertEqual(cement, construction.cement)
            self.assertEqual(brick, construction.brick)

    def test_construction_prices(self):
        price = Prices()

        for floors in range(0, 20):
            construction = Construction(floors)
            brick_price = price.brick_for(construction.brick)
            cement_price = price.cement_for(construction.cement)

            self.assertEqual(
                construction.price_for_each_meter, brick_price + cement_price
            )
