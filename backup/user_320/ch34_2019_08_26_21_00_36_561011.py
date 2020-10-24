mont = float(input('Digite o valor do depósito inicial: '))
juros = float(input('Digite o valor da tx de juros: '))
inicio = mont

for i in range(1, 25):
    print( mont)
    mont *= 1 + juros
    
print(mont - inicio)