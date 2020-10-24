import math

r = 10

def calcula_volume_da_esfera(r):
    v = 4/3*math.pi*r**3
    return v

print(calcula_volume_da_esfera(r))