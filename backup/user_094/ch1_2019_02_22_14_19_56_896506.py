# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 10:21:09 2019

@author: biamc
"""

def calcula_valor_devido(valoremprestado,taxadejuros,númerodemeses):
    y = valoremprestado*(1+taxadejuros)**númerodemeses
    return y

