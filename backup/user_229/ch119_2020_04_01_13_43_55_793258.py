import math
def calcula_euler(i,s):
    i = 0
    s = 0
    for i in range(s+1):
        s += (x**i)/math.factorial(i)
        print(s)
    return s
print(calcula_euler)