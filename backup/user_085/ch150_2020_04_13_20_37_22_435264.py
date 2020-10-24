import math
def calcula_pi(n):
    i = 1
    pi = (6/i**2)
    if n == 1:
        pi = (6/1**2)
    else:
        while i <= n:
            i += 1
            pi += (6/i**2)
    py  = math.sqrt(pi)
    return py