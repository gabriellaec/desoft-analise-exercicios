import math
def volume_da_pizza(z, a):
    volume = (math.pi * (z ** 2)) * a
    return volume

resposta = volume_da_pizza(20, 3)
print(resposta)