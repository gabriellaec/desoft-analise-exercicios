mont = float(input('Digite o valor do depósito inicial: '))
juros = float(input('Digite o valor da tx de juros: '))
inicio = mont

for i in range(1, 25):
    mont *= 1 + juros
    print(round(mont, 2))
    
    
print(round(mont - inicio, 2))