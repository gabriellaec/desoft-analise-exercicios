def calcula_valor_devido ( valor, taxa, meses):
    m= valor*(1+taxa)**meses
    return m

valor=1000
taxa=2
meses=3
print(calcula_valor_devido(valor,taxa,meses))
