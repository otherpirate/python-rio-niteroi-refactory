from __future__ import absolute_import
import unittest
from src_refactory.main import tabela_de_preco, define_cimento, cotacao_por_m2, \
    main



class MainTests(unittest.TestCase):

    def setUp(self):
        self.configuracao = {}

    def test_tabela_precos(self):
        tabela = tabela_de_preco()
        self.assertIn('tijolo', tabela)
        self.assertIn('cimento', tabela)

        tabela_tijolos = tabela['tijolo']
        self.assertIn('4 furos', tabela_tijolos)
        self.assertIn('8 furos', tabela_tijolos)
        self.assertIn('12 furos', tabela_tijolos)

        tabela_cimentos = tabela['cimento']
        self.assertIn('fino', tabela_cimentos)
        self.assertIn('medio', tabela_cimentos)
        self.assertIn('forte', tabela_cimentos)

    def test_define_cimento_fino(self):
        self.configuracao['tijolo'] = '4 furos'
        self.assertNotIn('cimento', self.configuracao)

        define_cimento(self.configuracao)
        self.assertIn('cimento', self.configuracao)
        self.assertEqual(self.configuracao['cimento'], 'fino')

    def test_define_cimento_medio(self):
        self.configuracao['tijolo'] = '8 furos'
        self.assertNotIn('cimento', self.configuracao)

        define_cimento(self.configuracao)
        self.assertIn('cimento', self.configuracao)
        self.assertEqual(self.configuracao['cimento'], 'medio')

    def test_define_cimento_forte(self):
        self.configuracao['tijolo'] = '12 furos'
        self.assertNotIn('cimento', self.configuracao)

        define_cimento(self.configuracao)
        self.assertIn('cimento', self.configuracao)
        self.assertEqual(self.configuracao['cimento'], 'forte')

    def test_define_cimento_nao_cadastrado(self):
        self.configuracao['tijolo'] = '10 furos'
        self.assertNotIn('cimento', self.configuracao)

        define_cimento(self.configuracao)
        self.assertIn('cimento', self.configuracao)
        self.assertEqual(self.configuracao['cimento'], 'nao existe')

    def test_cotar_preco(self):
        self.configuracao['tijolo'] = '12 furos'
        define_cimento(self.configuracao)
        cotacao = cotacao_por_m2(self.configuracao)

        precos = tabela_de_preco()
        preco_tijolo = precos['tijolo']['12 furos']
        preco_cimento = precos['cimento']['forte']

        self.assertEqual(cotacao, preco_tijolo + preco_cimento)

    def test_calcula_para_ate_tres_andares(self):
        precos = tabela_de_preco()
        preco_tijolo = precos['tijolo']['4 furos']
        preco_cimento = precos['cimento']['fino']

        for andar in range(1, 4):
            cotacao = main(andares=andar)
            self.assertEqual(cotacao, preco_cimento + preco_tijolo)

    def test_calcula_de_quatro_a_dez_andares(self):
        precos = tabela_de_preco()
        preco_tijolo = precos['tijolo']['8 furos']
        preco_cimento = precos['cimento']['medio']

        for andar in range(4, 11):
            cotacao = main(andares=andar)
            self.assertEqual(cotacao, preco_cimento + preco_tijolo)

    def test_calcula_mais_de_dez_andares(self):
        precos = tabela_de_preco()
        preco_tijolo = precos['tijolo']['12 furos']
        preco_cimento = precos['cimento']['forte']

        for andar in range(11, 21):
            cotacao = main(andares=andar)
            self.assertEqual(cotacao, preco_cimento + preco_tijolo)
