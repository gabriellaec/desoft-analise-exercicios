import math
def calcula_pi(n):
    sum = 0
    i = 1
    for i in range(n):
        sum += (6/i**2)
    return math.sqrt(sum)