import math
def calcula_pi (n):
    i = 1
    y = 0
    while 1<= i <= n:
        y += 6/(i**2)
        i += 1
    return math.sqrt(y)