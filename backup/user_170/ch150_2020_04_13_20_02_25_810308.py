import math
def calcula_pi(n):
    fraction = 0
    i = 1
    while i <= n:
        fraction += (6/(i**2))
        i+=1
    pi = math.sqrt(fraction)
    return pi
