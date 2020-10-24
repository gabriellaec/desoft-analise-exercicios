def snell_descartes (N1,N2,O1) :
    O2 = O1*N1/N2
    return O2


N1 = 10
N2 = 2
O1 = 60
O2 =snell_descartes(N1,N2,O1)
print("O2 =",O2)
