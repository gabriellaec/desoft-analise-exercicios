import math
def snell_descartes (N1,N2,O1):
    O1 = math.sin(math.radians(O1))
    O2 = math.degrees(math.asin(O1*N1/N2))
    return O2