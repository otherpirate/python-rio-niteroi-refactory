import sys
import inspect


def brick_factory(floors):
    final_class = None
    klasses = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for klass in klasses:
        klass = klass[1]
        if klass.MAX_FLOORS >= floors:
            if not final_class:
                final_class = klass

            if klass.MAX_FLOORS <= final_class.MAX_FLOORS:
                final_class = klass

    return final_class()


class BrickAbstract(object):
    MAX_FLOORS = 0
    def __init__(self, name, cement):
        self._name = name
        self._cement = cement

    @property
    def cement(self):
        return self._cement

    @property
    def name(self):
        return self._name


class BrickSmall(BrickAbstract):
    MAX_FLOORS = 3
    def __init__(self):
        super(BrickSmall, self).__init__('4 furos', 'fino')


class BrickMedium(BrickAbstract):
    MAX_FLOORS = 10
    def __init__(self):
        super(BrickMedium, self).__init__('8 furos', 'medio')


class BrickBig(BrickAbstract):
    MAX_FLOORS = 30
    def __init__(self):
        super(BrickBig, self).__init__('12 furos', 'forte')
