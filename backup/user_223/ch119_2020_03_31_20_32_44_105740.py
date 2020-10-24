import math
def calcula_euler(x,n):
	k = 0
	euler = []
	while k < n:
	    y = x + x**(k)/math.factorial(k)
	    euler.append(y)
	    k += 1
	    return (euler)
	soma_euler = sum(euler)
	return soma_euler