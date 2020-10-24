import math
def calcula_euler(x ,n):
    enn = 0.0
    exn = 0.0
    for i in range (n):
        exn = exn +( x**i / math.factorial(i))   
    return exn

    