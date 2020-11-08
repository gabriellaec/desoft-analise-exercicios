# -*- coding: utf-8 -*-
import math
def calcula_gaussiana(x,u,j):
    aux1 = (x - u) / j
    aux2 = -0.5 * aux1**2
    aux3 = 1.0/(j*math.sqrt(math.pi*2))
    aux4 = aux3 * math.exp(aux2)
    return aux4

