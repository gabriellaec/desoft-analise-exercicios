#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 17:34:01 2019

@author: thiagopegorer
"""

with open ("churras.txt","r") as arquivo:
    conteudo=arquivo.read()

linhas=conteudo.split('\n')

total=0
for l in linhas:
    colunas=l.split(",")
    soma=float(colunas[1])*float(colunas[2])
    total=total+soma
print(total)
    
    
    