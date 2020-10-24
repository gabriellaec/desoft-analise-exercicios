potencia = 0
soma = 0
while potencia < 100:
    soma = soma + 1/(2**potencia)
    potencia += 1
print(soma)