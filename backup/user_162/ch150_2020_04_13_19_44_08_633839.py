from math import *

#p = aproximação de pi

def calcula_pi(n):
    p = 0
    for i in range(1, n):
        p += 6/(i**2)
    return sqrt(p)
