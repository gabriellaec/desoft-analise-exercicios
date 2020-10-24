def calcular_valor_devido(valor, meses, juros):
    vf = valor*(1+juros/100)**meses
    return vf

valor=float(input("Qual é o valor emprestado?"))
meses=int(input("Quantos meses"))
juros=float(input("Qual a taxa de juros?"))

print(calcular_valor_devido(100,12,1))