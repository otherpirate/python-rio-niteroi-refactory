from __future__ import absolute_import
from src_refactory.brick import brick_factory
from src_refactory.cement import cement_factory


class Construction(object):

    def __init__(self, floors):
        self.floors = floors
        self._brick = brick_factory(self.floors)
        self._cement = cement_factory(self._brick)

    @property
    def brick(self):
        return self._brick.name

    @property
    def cement(self):
        return self._cement.name

    @property
    def price_for_each_meter(self):
        return self._cement.price + self._brick.price
