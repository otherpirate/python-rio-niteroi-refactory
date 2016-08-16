from __future__ import absolute_import
import unittest
from src_refactory.cement import cement_factory, CementTiny, CementMedium, \
    CementStrong, CementBrutal
from src_refactory.brick import BrickSmall, BrickMedium, BrickHuge, BrickBig


class CementTests(unittest.TestCase):

    def test_cement_tiny(self):
        cement = CementTiny()
        self.assertEqual(cement.name, 'fino')
        self.assertEqual(cement.price, 0.2)

    def test_cement_medium(self):
        cement = CementMedium()
        self.assertEqual(cement.name, 'medio')
        self.assertEqual(cement.price, 0.4)

    def test_cement_strong(self):
        cement = CementStrong()
        self.assertEqual(cement.name, 'forte')
        self.assertEqual(cement.price, 0.5)

    def test_cement_brutal(self):
        cement = CementBrutal()
        self.assertEqual(cement.name, 'brutal')
        self.assertEqual(cement.price, 0.9)

    def test_factory_tiny(self):
        cement = cement_factory(BrickSmall())
        self.assertIsInstance(cement, CementTiny)

    def test_factory_medium(self):
        cement = cement_factory(BrickMedium())
        self.assertIsInstance(cement, CementMedium)

    def test_factory_strong(self):
        cement = cement_factory(BrickBig())
        self.assertIsInstance(cement, CementStrong)

    def test_factory_brutal(self):
        cement = cement_factory(BrickHuge())
        self.assertIsInstance(cement, CementBrutal)

