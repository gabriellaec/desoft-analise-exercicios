from math import sqrt

def calcula_pi(n):
    
    radicando = 0
    
    for i in range(n):
        print(i)
        radicando += 6 / n ** 2
    
    return sqrt(radicando)