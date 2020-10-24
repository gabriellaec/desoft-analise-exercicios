import math
def calcula_euler(x,n):
    i = 0
    soma = 0
    while i<n:
    	f = math.factorial(i)
    	soma += (x**i)/f
        i += 1
    return soma