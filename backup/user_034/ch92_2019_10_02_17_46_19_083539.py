# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 14:14:32 2019

@author: enzos
Questao 3 -P.I.
"""
def simplifica_dict(dicionario):
    lista=[]
    for e in dicionario:
        if e not in lista:
            lista.append(e)
    return lista
