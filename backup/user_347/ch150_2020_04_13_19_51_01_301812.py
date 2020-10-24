import math
def calcula_pi(n):
    i = 1
    num = 0
    while i <= n:
        num += 6/(i**2)
        i += 1
    x = math.sqrt(num + (6/(n**2)))
    return x
        