import math
def calcula_pi(n):
    sum = 0
    i = 1
    print(n)
    print(i)
    for i in range(n - 1):
        print(i)
        sum += (6/i**2)
        print(i)
    return math.sqrt(sum)