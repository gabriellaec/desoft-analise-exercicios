import math
def calcula_pi(n):
    x = 1
    p = 0
    while x<=n:
        p += (6/(x**2))
        x += 1
    pi = math.sqrt(p)
    return p