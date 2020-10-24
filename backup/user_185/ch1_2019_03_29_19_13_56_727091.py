# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:34:53 2019

@author: RafaelzZ
"""

def calcula_valor_devido(valor_devido,valor_emprestado,taxa_de_juros,número_de_meses):
    valor_devido = valor_emprestado*(1+taxa_de_juros)**número_de_meses
    return valor_devido


