import math
def calcula_euler(x,n):
    conta = 0
    eq = 1 + x
    i = 2
    while n >= i:
        conta = conta + (x ** i) / math.factorial(i)
        i += 1
    final = eq + conta
    return final