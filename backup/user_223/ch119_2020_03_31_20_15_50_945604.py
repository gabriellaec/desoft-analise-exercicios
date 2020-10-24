import math
def calcula_euler(x,n):
	k = 0
    for n > 2:
	    while k < (n-1):
		    y = 1 + x + (x**((n-2)-k)/math.factorial((n-2)-k))
		    return (y)
		    k += 1
    else: 
        y = 1 + x
        return y