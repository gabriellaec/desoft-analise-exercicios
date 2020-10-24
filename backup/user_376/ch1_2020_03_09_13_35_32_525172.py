def calcula_valor_devido(C,N,I):
    calcula_valor_devido = C*((1+I)**N)
    return calcula_valor_devido
print ("o montante será de ", calcula_valor_devido(C,N,I))