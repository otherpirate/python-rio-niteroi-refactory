from __future__ import absolute_import
from src_refactory.prices import Prices
from src_refactory.brick import brick_factory


class Construction(object):

    def __init__(self, floors):
        self.floors = floors
        self._brick = brick_factory(self.floors)


    @property
    def brick(self):
        return self._brick.name

    @property
    def cement(self):
        return self._brick.cement


    @property
    def price_for_each_meter(self):
        prices = Prices()
        return prices.cement_for(self.cement) + prices.brick_for(self.brick)
