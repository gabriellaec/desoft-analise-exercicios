# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:23:44 2019

@author: User
"""

def PrecoPassagem (d):
    if (d<=200):
        v = d*0.50
        return v
    else:
        v = 100 + ((d - 200)*0.45)
        return v

distancia = int(input("Quantos km você deseja percorrer? "))
print ("Você pagará R$:",PrecoPassagem(distancia))