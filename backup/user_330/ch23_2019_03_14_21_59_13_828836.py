#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 10:33:10 2019

@author: ellenbeatriz
"""

def verifica_idade(idade):
    if idade >= 21:
        return 'Liberado EUA e BRASIL'
    else:
        if idade >= 18:
            return 'Liberado BRASIL'
        else:
            return 'Não está liberado' 

print(testa_maioridade(34))

"""
def testa_maioridade2(idade):
    if idade >= 21:
        return 'Liberado EUA e BRASIL'
    
    elif idade >= 18:
        return 'Liberado BRASIL'
    
    else:
        return 'Não está liberado'
        
print(testa_maioridade2(16))
"""
