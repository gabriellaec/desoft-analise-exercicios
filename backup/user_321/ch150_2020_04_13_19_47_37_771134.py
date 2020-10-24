import math
def calcula_pi(n):
    i = 0
    pi = 0
    while i != n:
        pi += 6/i**2
        i += 1
    return math.sqrt(pi)