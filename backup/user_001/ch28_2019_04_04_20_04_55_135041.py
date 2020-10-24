# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:22:01 2019

@author: Admin
"""

def verifica_idade(idade):
    if idade < 18:
        return "Não está liberado"
    elif idade < 21:
        return "Liberado BRASIL"
    else:
        return "Liberado EUA e BRASIL"