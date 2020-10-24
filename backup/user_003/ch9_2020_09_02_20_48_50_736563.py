import math
def calcula_volume_da_esfera(R):
    v = (4/3) * math.pi * R ** 3
    return v

R = 1
v = calcula_volume_da_esfera(R)
print(v)