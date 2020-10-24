# -*- coding: utf-8 -*-
"""
programa de teste para "string"

@author: Francisco Janela
"""

def asteriscos(n):
    asteriscos=n*str("*")
    return asteriscos

numero_asteriscos=input('quantos asteriscos? ')

print(asteriscos(int(numero_asteriscos)))