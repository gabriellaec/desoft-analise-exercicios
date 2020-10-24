import math
import numpy
def PiWallis(n):
    elemento = [0]*n
    i = 0
    while i < n:
        if i%2 == 0:
            elemento[i] = 2*i/(2*i-1)
        else:
            elemento[i] = 2*i/(2*i+1)
        i+=1
    y = numpy.prod(elemento)
    return y