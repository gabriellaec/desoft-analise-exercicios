import math
def calcula_volume_da_esfera(R) :
    y = ((R**3)*math.pi)*4/3
    return y
R = 2
y = calcula_volume_da_esfera(R)
print (y)
