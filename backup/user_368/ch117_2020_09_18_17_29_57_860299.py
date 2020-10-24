import math
def snell_descartes (N1,N2,O1) :
    O1 = radians(O1)
    O2 = O1*N1/N2
    O2 = degree(O2)
    return O2