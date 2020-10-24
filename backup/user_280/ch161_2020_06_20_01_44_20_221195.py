import math
def PiWallis(n):
    elemento = [0]*n
    elemento[0] = 1
    i = 1
    while i < n:
        if i%2 == 0:
            elemento[i] = i/(i+1)
        else:
            elemento[i] = (i+1)/i
        i+=1    
    produto = 1
    for numero in elemento:
        produto *= numero
    return 2*produto