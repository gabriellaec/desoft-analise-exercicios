import math
def calcula_euler(x,n):
    e_x = 0
    for i in range(0, n):
        print(i)
        e_x = e_x + ((x)^i)/(math.factorial(i))
        print(e_x)

    return e_x
 