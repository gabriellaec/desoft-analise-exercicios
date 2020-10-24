mont = float(input('Digite o valor do depósito inicial: '))
aport = float(input('Digite o valor do depósito mensal: '))
juros = float(input('Digite o valor da tx de juros: '))

inicio = mont
mont += aport
for i in range(1, 25):
    mont *= 1 + juros
    mont += aport
    print(round(mont, 2))
print(round(mont - inicio, 2))