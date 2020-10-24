# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 16:00:40 2019

@author: User
"""
lista = [1,2,3,4]

def soma_valores(): 
    soma = 0 
    i = 0
    while i < len(lista):
        soma = lista[i] + soma
        i = i + 1
    return soma

print (soma_valores())