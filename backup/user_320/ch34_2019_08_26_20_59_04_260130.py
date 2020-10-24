mont = float(input('Digite o valor do depósito inicial: '))
juros = float(input('Digite o valor da tx de juros: '))
soma = 0
inicio = mont
for i in range(1, 25):
    print((1 + juros) * mont - mont)
    mont *= 1 + juros
    
print(mont - inicio)