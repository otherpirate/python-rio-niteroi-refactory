
class Prices(object):

    @property
    def cements(self):
        return {'fino': 0.2, 'medio': 0.4, 'forte': 0.5}

    @property
    def bricks(self):
        return {'4 furos': 0.6, '8 furos': 0.7, '12 furos': 0.9}

    def cement_for(self, cement_name):
        return self.cements[cement_name]

    def brick_for(self, brick_name):
        return self.bricks[brick_name]
