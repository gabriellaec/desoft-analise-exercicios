from math import sqrt 
def calcula_pi(n):
    i = 1
    soma = 0
    while i<=n:
        soma += sqrt(6/i**2)
        i+=1
    return soma 
     
        