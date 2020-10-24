import math
def calcula_pi(n):
    i = 1
    soma = 0
    while i <= n:
        x = 6/(i**2)
        soma = soma + x
        i=i+1
        
    print (math.sqrt(soma))
    return math.sqrt(soma)