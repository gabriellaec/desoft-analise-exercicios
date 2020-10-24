deposito_inicial = float(input())
deposito_mensal = float(input())
juros = float(input())

MESES = 24
meses = 0
total = deposito_inicial
while meses < MESES:
    total *= 1 + juros
    total += deposito_mensal
    print('{:.2f}'.format(total))
    meses += 1
print('{:.2f}'.format(total - deposito_inicial - MESES * deposito_mensal))
