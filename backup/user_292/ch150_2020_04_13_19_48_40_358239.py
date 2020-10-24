import math
def calcula_pi(n):
    pi = 0
    x = 1
    while x<=n:
        pi += math.sqrt(6/x**2)
        x+=1
    return pi