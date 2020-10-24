import math
k = 0
def calcula_euler(x,n):
	while k < n:
	    y = 1 + x + (x**(n-k)/math.factorial(n-k))
	    return y
	    k += 1