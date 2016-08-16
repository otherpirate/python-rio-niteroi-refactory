from __future__ import absolute_import
import unittest
from src_refactory.brick import brick_factory, BrickSmall, BrickMedium, BrickBig


class BrickTests(unittest.TestCase):

    def test_brick_small(self):
        brick = BrickSmall()
        self.assertEqual(brick.name, '4 furos')
        self.assertEqual(brick.price, 0.6)

    def test_brick_medium(self):
        brick = BrickMedium()
        self.assertEqual(brick.name, '8 furos')
        self.assertEqual(brick.price, 0.7)

    def test_brick_big(self):
        brick = BrickBig()
        self.assertEqual(brick.name, '12 furos')
        self.assertEqual(brick.price, 0.9)

    def test_factory_small(self):
        for floor in range(1, 4):
            brick = brick_factory(floor)
            self.assertIsInstance(brick, BrickSmall)

    def test_factory_medium(self):
        for floor in range(4, 11):
            brick = brick_factory(floor)
            self.assertIsInstance(brick, BrickMedium)

    def test_factory_big(self):
        for floor in range(11, 31):
            brick = brick_factory(floor)
            self.assertIsInstance(brick, BrickBig)
