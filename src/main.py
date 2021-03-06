def tabela_de_preco():
    return {
        'tijolo': {'4 furos': 0.6, '8 furos': 0.7, '12 furos': 0.9, '20 furos': 1.4},
        'cimento': {'fino': 0.2, 'medio': 0.4, 'forte': 0.5, 'brutal': 0.9},
    }


def define_cimento(configuracao):
    if configuracao['tijolo'] == '4 furos':
        configuracao['cimento'] = 'fino'
    elif configuracao['tijolo'] == '8 furos':
        configuracao['cimento'] = 'medio'
    elif configuracao['tijolo'] == '12 furos':
        configuracao['cimento'] = 'forte'
    elif configuracao['tijolo'] == '20 furos':
        configuracao['cimento'] = 'brutal'
    else:
        configuracao['cimento'] = 'Nao existe'


def cotacao_por_m2(configuracao):
    precos = tabela_de_preco()
    return precos['tijolo'][configuracao['tijolo']] + precos['cimento'][configuracao['cimento']]


def main(andares):
    configuracao = {}

    ## Escolhe o tijolo
    if andares < 3:
        configuracao['tijolo'] = '4 furos'
    elif andares >= 4 and andares <= 10:
        configuracao['tijolo'] = '8 furos'
    elif andares <= 30:
        configuracao['tijolo'] = '12 furos'
    elif andares > 30:
        configuracao['tijolo'] = '20 furos'

    # Define o cimento
    define_cimento(configuracao)

    return cotacao_por_m2(configuracao)


if __name__ == '__main__':
    print (main(andares=40))
