#funçao para calcular o volume de uma esfera
import math
def calcular_volume_espera(raio):
    volume = (4 / 3) * math.pi * (raio)**3
    return volume
r = 5
x = calcular_volume_espera(r)
print(x)


