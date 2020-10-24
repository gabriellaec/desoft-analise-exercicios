C=int(input("Valor emprestado "))
N=int(input("número de meses "))
I=int(input("taxa de juros "))
def calcula_valor_devido(C,N,I):
    calcula_valor_devido = C*((1+I)**N)
    return calcula_valor_devido
print ("o montante será de ", calcula_valor_devido(C,N,I))