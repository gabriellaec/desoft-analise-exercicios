a = int(input('Depósito inicial:   '))
b = int(input('Taxa de juros:   '))
i = 1
s = 0
while i <= 24:
    valor = a*(1 + b)**i
    print(valor)
    s += valor
    i += 1
print('{0:2f}'s)