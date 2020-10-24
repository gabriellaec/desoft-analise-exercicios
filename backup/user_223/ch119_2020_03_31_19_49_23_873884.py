import math
def calcula_euler(x,n):
    k = 0
	while k < n:
	    y = 1 + x + (x**(n-k)/math.factorial(n-k))
	    return y
	    k += 1