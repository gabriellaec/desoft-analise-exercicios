deposito_inicial = float(input())
deposito_mensal = float(input())
juros = float(input())

MESES = 24
meses = 0
total = deposito_inicial
while meses < MESES:
    total *= 1 + juros
    print('{:.2f}'.format(total))
    total += deposito_mensal
    meses += 1
print('{:.2f}'.format(total - deposito_inicial - MESES * deposito_mensal))