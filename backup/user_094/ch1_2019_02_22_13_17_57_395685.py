def calcular_valor_devido(valor0,juros,n):
    y = valor0*(1+juros)**n
    return y

valor0=100  #supondo que o valor inicial seja 100
juros=0.02  #supondo que a taxa de juros sexa de 2%
n=6			#supondo que o número de meses seja 6
print(calcular_valor_devido(valor0,juros,n))
