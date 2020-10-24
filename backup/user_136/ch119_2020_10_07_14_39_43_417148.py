import math
def calcula_euler(x, n):
    resultado= 0
    i= 0
    w= 1
    while i<=n:
        termo= x**i / math.factorial(i)
        resultado+= termo
        x= w + resultado
    return x