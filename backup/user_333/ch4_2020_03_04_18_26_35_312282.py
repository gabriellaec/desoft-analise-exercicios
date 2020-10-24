# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:17:02 2020

@author: franc
"""

def classifica_idade(idade):
    if idade <= 11:
        return 'crianca'
    elif 11<idade<18:
        return 'adolescente'
    else:
        return 'adulto'

idade=int(input('qual sua idade?R: '))
print('você é {0}'.format(classifica_idade(idade)))