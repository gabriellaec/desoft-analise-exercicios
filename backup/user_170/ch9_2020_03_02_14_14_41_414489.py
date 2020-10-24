import math

def calcula_volume_da_esfera(r):
    v = (4*(float(math.pi))*(r**3))/3
    return v

b = calcula_volume_da_esfera(5)
print (b)
