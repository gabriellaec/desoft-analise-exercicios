print('=============')
print('Qual é o valor atual de sua dívida?')
montante = float(input())
print('=============')
print('Qual é a taxa de juros em percentual? OBS: digite apenas o número. Exemplo: no caso de 1%, digite apenas 1.')
juros = float(input())
print('=============')
print('Em quantos meses pretende pagar?')
meses = float(input())
def calcula_valor_devido(montante, meses, juros):
    valor = montante*((1 + (juros/100))**meses)
    return valor
print('o valor que você estará devendo daqui a',meses,' será de ',calcula_valor_devido(montante, juros, meses))