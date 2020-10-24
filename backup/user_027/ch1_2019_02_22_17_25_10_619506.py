print('=============')
print('Qual o valor atual de sua divida?')
montante = float(input())
print('=============')
print('Qual a taxa de juros em percentual? OBS: digite apenas o n. Exemplo: no caso de 1%, digite apenas 1.')
juros = float(input())
print('=============')
print('Em quantos meses pretende pagar?')
meses = float(input())
def calcula_valor_devido(montante, meses, juros):
    valor = montante*((1 + (juros/100))**meses)
    return valor
print('o valor que voce estara devendo daqui a',int(meses),'meses sera ',calcula_valor_devido(montante, juros, meses))