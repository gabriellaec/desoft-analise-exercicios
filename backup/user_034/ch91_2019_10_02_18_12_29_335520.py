# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 13:46:48 2019

@author: enzos
Questao 2 - P.I.
"""
with open('palavras.txt','r') as arquivo:
    lista_de_palavras = arquivo.readline()
i=0
for a in lista_de_palavras:
    lista_de_palavras.split() 
    if a.lower() == 'a':
        i+=1

print(i)

















