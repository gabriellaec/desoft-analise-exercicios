import math
def calcula_euler(x, n):
    w= 1
    q= 1
    u= 0
    p= 1
    i= 1
    while i<n:
        termo= x**i / math.factorial(i)
        resultado+= termo
        x= w + resultado
    return x