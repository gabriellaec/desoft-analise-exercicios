import math 

def calcula_volume_da_esfera (raio):
    vol = (4 * math.pi * (raio)**3)/3
    return vol

raio = 2 
x = calcula_volume_da_esfera (raio)
print (x) 
