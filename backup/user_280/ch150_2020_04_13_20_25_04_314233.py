import math
def calcula_pi(n):
    elemento = [0]*n
    i = 0
    while i < n:
        elemento[i] = 6/(i+1)**2
        i+=1
    y = sum(elemento)
    return math.sqrt(y)
    