import math
def calcula_euler(x,n):
    i = 1
    eq = 1
    while (i<n):
        eq = eq + (x**(n-i)/math.factorial(n-i))
        i = i+1
    return eq