aport = float(input('Digite o valor do depósito mensal: '))
mont = float(input('Digite o valor do aporte mensal: '))
juros = float(input('Digite o valor da tx de juros: '))
inicio = mont

for i in range(1, 25):
    mont *= 1 + juros
    print(round(mont, 2))
    mont += aport
print(round(mont - (inicio + (aport * 23)), 2))