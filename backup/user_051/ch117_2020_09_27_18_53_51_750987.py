import math as mt
def snell_descartes(n1, n2, O1):
    O2=(mt.sin(mt.radians(O1))*n1)/n2
    y=mt.sin(O2)
    x=mt.degrees(y)
    return x