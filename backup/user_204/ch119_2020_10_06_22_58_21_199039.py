import math
def calcula_euler(x,n):
    eq = 1 + x
    i = 2
    while n >= i:
        eq2 += (x ** i) / math.factorial(i)
        
    final = eq + eq2
    return final