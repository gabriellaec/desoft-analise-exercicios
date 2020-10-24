import math
def PiWallis(n):
    elemento = [0]*n
    elemento[0] = 2
    elemento[1] = 2/3
    i = 2
    while i < n:
        if i%2 == 0:
            elemento[i] = 2*i/(2*i-1)
        else:
            elemento[i] = 2*i/(2*i+1)
        i+=1    
    produto = 1
    for numero in elemento:
        produto *= numero
    return 2*produto