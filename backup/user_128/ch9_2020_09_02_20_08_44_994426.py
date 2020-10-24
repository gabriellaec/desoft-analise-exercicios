import math
def calcula_volume_da_esfera(r):
    volume = (4 * math.pi * (r ** 3)) / 3
    return volume

resposta = calcula_volume_da_esfera(20)
print(resposta)
