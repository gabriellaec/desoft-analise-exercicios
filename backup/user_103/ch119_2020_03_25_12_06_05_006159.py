import math
numerodetermos=1
def calcula_euler(x,n):
    exp=0
    soma = 0
    while exp < numerodetermos:
        soma+=x**exp/math.factorial(exp)
        exp+=1
    return soma