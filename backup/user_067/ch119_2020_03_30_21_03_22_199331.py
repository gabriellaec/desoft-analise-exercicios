import math
def calcula_euler(x,n):
    e_x = 1 + x
    for i in range(2, n+1):
        print(i)
        e_x = e_x + ((x)^i)/(math.factorial(i))
        print(e_x)

    return e_x
 