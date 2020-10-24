import math
def calcula_volume_da_esfera(r):
    y = (4/3)*math.pi*r**3
    return y
v = 3
j = calcula_volume_da_esfera(v)
print(j)