from __future__ import absolute_import
import unittest
from src_refactory.construction import Construction
from src_refactory.brick import brick_factory
from src_refactory.cement import cement_factory


class ConstructionTests(unittest.TestCase):

    def test_construction_attributes(self):
        construction = Construction(3)
        self.assertIsInstance(construction.floors, int)
        self.assertIsInstance(construction.cement, str)
        self.assertIsInstance(construction.brick, str)

    def test_construction_one_to_three_floors(self):
        for floors in range(1, 31):
            brick = brick_factory(floors)
            cement = cement_factory(brick)

            construction = Construction(floors)
            self.assertEqual(cement.name, construction.cement)
            self.assertEqual(brick.name, construction.brick)

    def test_construction_prices(self):
        for floors in range(1, 20):
            construction = Construction(floors)

            brick_price = construction._brick.price
            cement_price = construction._cement.price

            self.assertEqual(
                construction.price_for_each_meter, brick_price + cement_price
            )
