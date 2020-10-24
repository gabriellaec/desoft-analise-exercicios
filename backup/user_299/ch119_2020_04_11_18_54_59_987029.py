import math
from random import randint

def calcula_euler (x,n):
    e_elevado_a_x=0
    termos = [1]*n
    for i,e in enumerate(termos):
        termos[i]=(x**i)/math.factorial(i)
        e_elevado_a_x=e_elevado_a_x+termos[i]
    return e_elevado_a_x
