a = int(input('Depósito inicial:   '))
b = int(input('Taxa de juros:   '))
i = 1
s = 0
valor = a
while i <= 24:
    valor = valor + valor * b**i
    print(valor)
    s += valor
    i += 1
print('{0:2f}'s)