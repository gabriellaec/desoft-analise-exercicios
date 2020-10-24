import math
def calcula_euler (x, n):
    if n == 1:
        y = 1
        return y
    elif n == 2:
        y = 1 + x
        return y
    else:
        lista = [0] * n
        lista [0] = 1
        lista [1] = x
        i = 2
        while i < n:
            lista [i] = (x**2) / math.factorial (i)
            i += 1
        y = sum (lista)
        return y
x = 2
n = 4
resultado = calcula_euler (x, n)
print (n)
print (resultado)