from __future__ import absolute_import
from src_refactory.prices import Prices


class Construction(object):

    def __init__(self, floors):
        self.floors = floors

    @property
    def brick(self):
        if self.floors <= 3:
            return '4 furos'
        elif self.floors >= 4 and self.floors <= 10:
            return '8 furos'
        return '12 furos'

    @property
    def cement(self):
        if self.brick == '4 furos':
            return 'fino'
        elif self.brick == '8 furos':
            return 'medio'
        elif self.brick == '12 furos':
            return 'forte'

    @property
    def price_for_each_meter(self):
        prices = Prices()
        return prices.cement_for(self.cement) + prices.brick_for(self.brick)
