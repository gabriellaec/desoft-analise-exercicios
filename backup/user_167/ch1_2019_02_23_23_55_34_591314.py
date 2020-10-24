def calcula_valor_devido(emprestado,meses,juros):
    montante= emprestado*(1+juros)**meses
    return montante
a=10
b=5
c=0.2
print(calcula_valor_devido(a,b,c))