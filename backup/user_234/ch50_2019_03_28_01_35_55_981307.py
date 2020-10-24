#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:33:29 2019

@author: Juan
"""

lista_ind=[]



def numero_no_indice(lista):
    num_lista=len(lista)
    i = 0
    while i < num_lista:
        if lista[i] == i:
            lista_ind.append(lista[i])
            i+=1
        else:
            i+=1
    return lista_ind

print(numero_no_indice([1, 1, 2, 3]))