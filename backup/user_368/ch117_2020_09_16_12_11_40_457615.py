def calcula_O2 (N1,N2,O1) :
    O2 = O1*N1/N2
    return O2


N1 = int(input('Qual o valor de N1?'))
N2 = int(input('Qual o valor de N2?'))
O1 = int(input('Qual o valor de O1?'))
O2 =calcula_O2(N1,N2,O1)
print("O2 =",O2)
