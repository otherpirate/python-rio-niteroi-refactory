from __future__ import absolute_import
import sys
import inspect
from src_refactory.brick import BrickSmall, BrickMedium, BrickBig


def cement_factory(brick):
    klasses = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for klass in klasses:
        klass = klass[1]
        if 'Cement' in str(klass):
            if brick.__class__ in klass.BRICK_TYPE:
                return klass()


class CementAbstract(object):
    BRICK_TYPE = []
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


class CementTiny(CementAbstract):
    BRICK_TYPE = [BrickSmall]
    def __init__(self):
        super(CementTiny, self).__init__('fino')


class CementMedium(CementAbstract):
    BRICK_TYPE = [BrickMedium]
    def __init__(self):
        super(CementMedium, self).__init__('medio')


class CementStrong(CementAbstract):
    BRICK_TYPE = [BrickBig]
    def __init__(self):
        super(CementStrong, self).__init__('forte')
