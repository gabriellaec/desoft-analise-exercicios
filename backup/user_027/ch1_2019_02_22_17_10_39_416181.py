montante = float(input())

juros = float(input())

meses = float(input())
def calcula_valor_devido(montante, meses, juros):
    valor = montante*((1 + (juros/100))**meses)
    return valor
print('o valor que você estará devendo daqui a',int(meses),'meses será de ',calcula_valor_devido(montante, juros, meses))