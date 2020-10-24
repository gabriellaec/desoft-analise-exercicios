def calcula_valor_devido(montante, meses, juros):
    valor = montante*((1 + (juros/100))**meses)
    return valor
print('o valor que você estará devendo daqui a',meses,' será de ',calcula_valor_devido(montante, juros, meses))