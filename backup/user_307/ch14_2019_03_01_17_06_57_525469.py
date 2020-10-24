#Faça uma função que calcule o volume de uma esfera de raio R=(4/3)math.pi*r**3
#O nome da sua função deve ser calcula_volume_da_esfera.
import math
r=10
def calcula_volume_da_esfera(r):
	R=(4/3)*math.pi*r**3
	return R
print (calcula_volume_da_esfera(r))