from __future__ import absolute_import
import unittest
from src_refactory.prices import Prices
from src_refactory.main import define_cimento, cotacao_por_m2, \
    main



class MainTests(unittest.TestCase):

    def setUp(self):
        self.configuracao = {}
        self.prices = Prices()

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

        preco_tijolo = self.prices.brick_for('12 furos')
        preco_cimento = self.prices.cement_for('forte')

        self.assertEqual(cotacao, preco_tijolo + preco_cimento)

    def test_calcula_para_ate_tres_andares(self):
        preco_tijolo = self.prices.brick_for('4 furos')
        preco_cimento = self.prices.cement_for('fino')

        for andar in range(1, 4):
            cotacao = main(andares=andar)
            self.assertEqual(cotacao, preco_cimento + preco_tijolo)

    def test_calcula_de_quatro_a_dez_andares(self):
        preco_tijolo = self.prices.brick_for('8 furos')
        preco_cimento = self.prices.cement_for('medio')

        for andar in range(4, 11):
            cotacao = main(andares=andar)
            self.assertEqual(cotacao, preco_cimento + preco_tijolo)

    def test_calcula_mais_de_dez_andares(self):
        preco_tijolo = self.prices.brick_for('12 furos')
        preco_cimento = self.prices.cement_for('forte')

        for andar in range(11, 21):
            cotacao = main(andares=andar)
            self.assertEqual(cotacao, preco_cimento + preco_tijolo)
