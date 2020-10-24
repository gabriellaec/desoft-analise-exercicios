import math
def calcula_euler(x,n):
    e_x = 1
    for i in range(1, n+1):
        print(i)
        e_x = e_x + ((x)^i)/(math.factorial(i))
        print(e_x)

    return e_x
 