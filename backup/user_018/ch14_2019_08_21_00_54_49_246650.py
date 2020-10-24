#Função que calcule o volume de uma esfera

import math 

def calcula_volume_esfera (raio):
    vol = (4 * math.pi * (raio)**3)/3
    return vol

raio = 2 
x = calcula_volume_esfera (raio)
print (x) 
