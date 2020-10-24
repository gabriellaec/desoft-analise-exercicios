import math as mt
def snell_descartes(n1, n2, O1):
    a=mt.radians(O1)
    O2=mt.degrees(mt.sin(mt.sin(a)*n1/n2))
    return O2