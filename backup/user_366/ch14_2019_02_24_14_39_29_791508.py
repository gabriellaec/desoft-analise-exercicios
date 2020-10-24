import math

def calcula_volume_da_esfera(raio):
    v = 4*math.pi*raio**3/3
    return v
a = 10;
b = calcula_volume_da_esfera(a);
print(b);