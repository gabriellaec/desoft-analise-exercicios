import math 
def calcula_volume_esfera (r):
    y = 4/3 *math.pi*r**3
    return y

a=2
V= calcula_volume_esfera(a)

print(V)