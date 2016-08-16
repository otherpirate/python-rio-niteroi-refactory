from __future__ import absolute_import
import sys
import inspect
from src_refactory.brick import BrickSmall, BrickMedium, BrickBig, BrickHuge


def cement_factory(brick):
    klasses = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for klass in klasses:
        klass = klass[1]
        if 'Cement' in str(klass):
            if brick.__class__ in klass.BRICK_TYPE:
                return klass()


class CementAbstract(object):
    BRICK_TYPE = []
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price


class CementTiny(CementAbstract):
    BRICK_TYPE = [BrickSmall]
    def __init__(self):
        super(CementTiny, self).__init__('fino', 0.2)


class CementMedium(CementAbstract):
    BRICK_TYPE = [BrickMedium]
    def __init__(self):
        super(CementMedium, self).__init__('medio', 0.4)


class CementStrong(CementAbstract):
    BRICK_TYPE = [BrickBig]
    def __init__(self):
        super(CementStrong, self).__init__('forte', 0.5)


class CementBrutal(CementAbstract):
    BRICK_TYPE = [BrickHuge]
    def __init__(self):
        super(CementBrutal, self).__init__('brutal', 0.9)
