import math
def calcula_volume_da_esfera (R):
    V=4/3*(math.pi*(R**3))
    return V
R=3
V= calcula_volume_da_esfera (R)
print (V)