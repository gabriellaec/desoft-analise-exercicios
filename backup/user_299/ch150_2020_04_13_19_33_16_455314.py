def calcula_pi(n):
    import math
    termos = [1]*n
    soma = 0
    for i, e in enumerate(termos):
        e = 6/((i+1)**2) 
        soma = soma + e
    pi = math.sqrt(soma)  
    return pi