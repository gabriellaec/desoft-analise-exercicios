#funçao para calcular o volume de uma esfera
import math
def calcula_volume_da_espera(raio):
    volume = (4 / 3) * math.pi * (raio)**3
    return volume
r = 5
x = calcula_volume_da_espera(r)
print(x)


