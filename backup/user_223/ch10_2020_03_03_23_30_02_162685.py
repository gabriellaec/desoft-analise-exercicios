import math
def volume_da_pizza(raio, altura):
	volume = math.pi*raio**2*altura
	return volume
print (volume_da_pizza(5, 2))