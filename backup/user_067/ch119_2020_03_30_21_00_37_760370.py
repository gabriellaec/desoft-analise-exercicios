import math
def calcula_euler(x,n):
    e_x = 0
    for i in range(0, n+1):
        print(i)
        e_x = e_x + (x^i)/math.factorial(i)

    return e_x
 