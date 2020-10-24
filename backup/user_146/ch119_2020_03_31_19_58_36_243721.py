import math
k = 0
i = 0
def calcula_euler(n,x):
    y = 1 + (x**(k+1)/(math.factorial(i+1)))*n
    return y
print(calcula_euler(10,20))