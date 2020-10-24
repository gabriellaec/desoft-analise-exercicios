dep = float(input('Digite o valor do depósito inicial: '))
juros = float(input('Digite o valor da tx de juros: '))
soma = 0
inicio = dep
for i in range(1, 25):
    print((1 + juros) * dep - inicio)
    dep *= 1 + juros
    
print(dep - inicio)