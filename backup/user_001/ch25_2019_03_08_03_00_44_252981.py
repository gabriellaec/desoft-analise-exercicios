# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 23:52:26 2019

@author: Admin
"""

def preco_passagem():
    
    n=int(input("digite a distancia em km:"))
    if n <= 200:
        return (n*0.5)
    return (((n-200)*0.45)+100)

print(preco_passagem())