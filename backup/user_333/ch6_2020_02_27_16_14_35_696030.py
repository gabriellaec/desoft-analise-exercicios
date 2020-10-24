# -*- coding: utf-8 -*-
"""
programa que transforme a temperatura dada em celsius para fahrenheit

@autor: Francisco Janela
"""
#a função utiliza a fórmula de conversão de celsius para fahrenheit
def celsius_para_fahrenheit(C):
    F=(C*9/5)+32
    return F

#através do input da temperatura em celsius, é feita a conversão para fahrenheit
temperatura_em_celsius=32
print('{0}°C equivalem a {1}°F.'.format(temperatura_em_celsius,celsius_para_fahrenheit(temperatura_em_celsius)))