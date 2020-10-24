import math
def PiWallis(n):
    k = n-1
    elemento = [0]*(k)
    elemento[0] = 2
    i = 1
    while i < k -1:
        if i%2 == 0:
            elemento[i] = (i+1)/(i+2)
        else:
            elemento[i] = (i+2)/(i+1)
        i+=1    
    produto = 1
    for numero in elemento:
        produto *= numero
    y = 2*produto
    return y