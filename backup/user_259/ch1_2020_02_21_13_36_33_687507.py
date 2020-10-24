# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 10:22:48 2020

@author: tprfe
"""

def calcula_valor_devido(valor_inicial):
    montante = valor_inicial*(1+taxa_de_juros)**tempo_de_aplicação
    return montante
valor = int(input("Valor inicial: "))
taxa_de_juros = (int(input("Taxa de juros: ")))/100
tempo_de_aplicação = int(input("Tempo de apliação: "))
m = calcula_valor_devido(valor)
print("O valor a ser pago é {0} reais".format(m))
