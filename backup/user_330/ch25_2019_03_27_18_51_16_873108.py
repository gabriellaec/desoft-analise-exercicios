#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 10:56:03 2019

@author: ellenbeatriz
"""
km = int(input("Quantos km deseja percorrer? " ))
def distancia(km):
    
    if km > 200 :
        resultado = 200*0.5 + (200-km)*0.45
        return resultado
    
    elif km <= 200:
        resultado = km*0.5
        return resultado

print(distancia(km))