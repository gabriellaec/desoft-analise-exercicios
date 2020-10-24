import math

def calcula_euler(x, n):
   
   lista = [0]*n   
   i = 0
   f = 0
   exp = 0
   soma = 0
   
   while i < n:
       lista[i] = (x**exp)/(math.factorial(f))
       exp += 1
       i += 1
       f += 1
       soma += lista[i] 
   
   return soma
