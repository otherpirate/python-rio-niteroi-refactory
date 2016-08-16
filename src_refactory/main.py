from __future__ import absolute_import
from src_refactory.prices import Prices

def define_cimento(configuracao):
    if configuracao['tijolo'] == '4 furos':
        configuracao['cimento'] = 'fino'
    elif configuracao['tijolo'] == '8 furos':
        configuracao['cimento'] = 'medio'
    elif configuracao['tijolo'] == '12 furos':
        configuracao['cimento'] = 'forte'
    else:
        configuracao['cimento'] = 'nao existe'


def cotacao_por_m2(configuracao):
    prices = Prices()
    return prices.brick_for(configuracao['tijolo']) + prices.cement_for(configuracao['cimento'])


def main(andares):
    configuracao = {}

    ## Escolhe o tijolo
    if andares <= 3:
        configuracao['tijolo'] = '4 furos'
    elif andares >= 4 and andares <= 10:
        configuracao['tijolo'] = '8 furos'
    else:
        configuracao['tijolo'] = '12 furos'

    # Define o cimento
    define_cimento(configuracao)

    return cotacao_por_m2(configuracao)


if __name__ == '__main__':
    print (main(andares=4))

