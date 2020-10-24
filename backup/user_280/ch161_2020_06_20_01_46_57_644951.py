import math
def PiWallis(n):
    elemento = [0]*(n+1)
    i = 0
    while i < n:
        if i%2 == 0:
            elemento[i] = i/(i+1)
        elif i == 0:
            elemento[i] = 1
        else:
            elemento[i] = (i+1)/i
        i+=1    
    produto = 1
    for numero in elemento:
        produto *= numero
    y = 2*produto
    return y