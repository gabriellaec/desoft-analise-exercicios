import math
def snell_descartes (N1,N2,O1):
    O1 = math.assin(math.sin(math.radians(O1)))
    O2 = math.degrees(O1*N1/N2)
    return snell_descartes