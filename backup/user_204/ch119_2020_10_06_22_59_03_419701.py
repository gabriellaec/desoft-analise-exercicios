import math
eq2 = 0
def calcula_euler(x,n):
    eq = 1 + x
    i = 2
    while n >= i:
        eq2 += (x ** i) / math.factorial(i)
        i += 1
    final = eq + eq2
    return final