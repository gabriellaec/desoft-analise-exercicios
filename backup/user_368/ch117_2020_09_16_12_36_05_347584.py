import math
def snell_descartes (N1,N2,O1) :
    O2 = O1*N1/N2
    return O2


N1 = 1
N2 = 2
O1 = math.sin(math.radians(30))
O2 = math.degrees(snell_descartes(N1,N2,O1))
print("O2 =",O2)