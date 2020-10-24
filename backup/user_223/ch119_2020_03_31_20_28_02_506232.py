import math
def calcula_euler(x,n):
	k = 0
	euler = []
	while k < n:
	    y = 1 + x + (x**(k)/math.factorial(k))
	    euler.append(y)
	    k += 1
	    soma_euler = sum(euler)
	    return soma_euler