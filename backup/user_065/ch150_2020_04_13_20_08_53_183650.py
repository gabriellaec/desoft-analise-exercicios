import math
def calcula_pi(n):
    sum = 0
    i = 1
    for i in range(n - 1):
        sum += (6/i**2)
        print(i)
    return math.sqrt(sum)