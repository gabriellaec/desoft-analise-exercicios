import math
def calcula_volume_da_esfera(r):
    y = (4/3)*math.pi*(r**3)
    return y
    
a = 5
resultado = calcula_volume_da_esfera(a)
print(resultado)