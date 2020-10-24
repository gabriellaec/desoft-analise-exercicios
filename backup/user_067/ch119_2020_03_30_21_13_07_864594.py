import math
def calcula_euler(x,n):
    e_x = 0
    
    for i in range(0, n):
        print(e_x)
        e_x = e_x + (x**i)/(math.factorial(i))
        
    return e_x
 