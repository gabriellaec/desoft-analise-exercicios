import math
def calcula_euler(x,n):
    i = 0
    soma = 0
    while i<n:
    	f = math.factorial(i)
        b = (x**i)/f
    	soma += b
        i += 1
    return soma