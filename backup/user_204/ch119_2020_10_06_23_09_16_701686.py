import math
def calcula_euler(x,n):
    conta = 0
    i = 2
    while n >= 3:
        conta = conta + (x ** i) / (math.factorial(i))
        i += 1
    final = 1 + x + conta
    return final
