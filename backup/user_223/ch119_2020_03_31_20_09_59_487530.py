import math
def calcula_euler(x,n):
	k = 0
	while k < (n-2):
		y = 1 + x + (x**((n-2)-k)/math.factorial((n-2)-k))
		return (y)
		k += 1