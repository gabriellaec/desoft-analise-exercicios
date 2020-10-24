import math
def calcula_pi(n):
    sum = 0
    n += 1
    for i in range(1, n):
        sum += (6/i**2)
    return math.sqrt(sum)