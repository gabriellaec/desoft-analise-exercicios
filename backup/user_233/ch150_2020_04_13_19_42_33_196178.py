from math import sqrt

def calcula_pi(n):
    
    radicando = 0
    
    for i in range(1, n + 1):
        radicando += 6 / i ** 2
    
    return sqrt(radicando)