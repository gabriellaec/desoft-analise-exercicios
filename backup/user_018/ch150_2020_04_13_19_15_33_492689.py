import math
def calcula_pi(n):
    i = 1
    soma = 0
    while i < n : 
        soma += 6/((n)**2)
        i+=1 
    pi = math.sqrt(soma)
    return pi
