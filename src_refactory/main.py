from __future__ import absolute_import
from src_refactory.construction import Construction


def calculate_price(floors):
    return Construction(floors).price_for_each_meter


if __name__ == '__main__':
    print (calculate_price(floors=4))
