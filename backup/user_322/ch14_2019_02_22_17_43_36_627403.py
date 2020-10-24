import math
def calcula_volume_da_esfera(raio):
    y = 4/3 * math.pi * raio ** 3
    return y

raio = 3
volume = calcula_volume_da_esfera(raio)
print(volume)