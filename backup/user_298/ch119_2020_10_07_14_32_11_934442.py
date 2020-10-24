import math
def calcula_euler(x,n):
    t = 0
    euler  = 1
    for t in range(0,n):
        euler += (x**t)/(math.factorial(t))
    return euler
print(calcula_euler(10,5))
