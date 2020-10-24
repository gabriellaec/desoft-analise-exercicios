import math
def calcula_euler(x,n):
soma=1
for i in range(1,n+1):
    soma=soma+(1/math.factorial(i))
return soma
