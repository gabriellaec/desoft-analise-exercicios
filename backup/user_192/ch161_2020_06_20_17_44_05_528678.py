import math
def PiWallis(n):
    elemento = [0]*(n)
    elemento[0] = 2
    i = 1
    while i < n:
        if i%2 == 0:
            elemento[i] = (i+2)/(i+1)
        else:
            elemento[i] = (i+1)/(i+2)
    produto = 1
    for numero in elemento:
        produto *= numero
    y = 2*produto
    return y
            