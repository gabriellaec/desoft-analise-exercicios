import math
def fatorial(n): 
   if n<=1:
      return 1
   else: 
      return n*fatorial(n-1)
def calcula_euler(x, n):
    resultado = math.exp(x)
    i = 0
    soma = 0 
    while i < n:
        soma = soma + (x**i)/fatorial(i)
        i += 1
    resultado = soma
    return resultado