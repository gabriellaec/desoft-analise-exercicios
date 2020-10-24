import math

def calcula_volume_da_esfera(r):
    Volume = (4/3)*math.pi*r**3
    return Volume
Resultado = calcula_volume_da_esfera(3)
print(Resultado)