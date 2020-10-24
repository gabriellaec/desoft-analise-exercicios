import math
from random import randint

def calcula_euler (x,n):
 i=0
 e_elevado_a_x=0
 termos = [1]*n
 while i<n:
 termos[i]=(x**i)/math.factorial(i)
 e_elevado_a_x=e_elevado_a_x+termos[i]
 i=i+1
 return e_elevado_a_x
