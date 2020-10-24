import math
def calcula_volume_da_esfera(R):
    volume_da_esfera= (4*math.pi*(R**3))/3
    return volume_da_esfera

r=4
volume= calcula_volume_da_esfera(r)
print(volume)