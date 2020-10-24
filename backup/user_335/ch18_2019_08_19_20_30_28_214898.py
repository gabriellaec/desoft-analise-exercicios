# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:08:52 2019

@author: User
"""

def encontra_cateto (h,c):
    vcateto = (((h**2)-(c**2))**(1/2))
    return vcateto

v1 = int(input("Digite um valor para a hipotenusa: "))
v2 = int(input("Digite um valor para um dos catetos: "))

resultado = encontra_cateto(v1,v2)
print (resultado)