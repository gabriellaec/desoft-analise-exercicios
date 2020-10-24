dep = float(input('Digite o valor do depósito inicial: '))
juros = float(input('Digite o valor da tx de juros: '))
soma = 0

for i in range(1, 25):
    print(f'{dep * (1 + juros) ** i:.02f}')
    soma += dep * (1 + juros) ** i
print(f'{soma - dep:.02f}')