import math
def calcula_euler(x,n):
	k = 0
	z = n-2
	while k < z:
		y = 1 + x + (x**((z)-k)/math.factorial((z)-k))
		return (y)
		k += 1