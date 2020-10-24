import numpy as np
import math 

graus = np.arange(0,90,1)

for x in range(len(graus)):
    lista = []
    seno_x = (4*x(180-x))/(40500 - x(180-x))
    mat = math.sin(x)
    diferenca = abs(seno_x - mat)

    lista.append(diferenca)

    print (graus[(lista.index(max(diferenca)))])