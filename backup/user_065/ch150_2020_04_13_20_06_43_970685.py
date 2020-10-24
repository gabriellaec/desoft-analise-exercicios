import math
def calcula_pi(n):
    sum = 0
    for i in range(n):
        sum += (6/i**2)
        print(i)
    return math.sqrt(sum)