# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 08:02:25 2019

@author: Fernando
"""

def calcula_valor_devido(valor_emprestado,numero_de_meses,taxas_de_juros):
       calcula_valor_devido = valor_emprestado*[(1 + taxas_de_juros)**numero_de_meses]
       return calcula_valor_devido
valor_emprestado=int(input('Valor emprestado: '))
taxas_de_juros=int(input('Taxas de juros: '))
numero_de_meses=int(input('Numero de meses: '))

print(calcula_valor_devido(valor_emprestado,numero_de_meses,taxas_de_juros))

