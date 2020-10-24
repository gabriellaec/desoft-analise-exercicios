import math.pi
def calcula_volume_da_esfera(R):
	v = (4/3)*math.pi*R**3
	return v

R = 5
vol = calcula_volume_da_esfera(R)
print(vol)