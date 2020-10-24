cont = 0
soma = 1/(2**cont)
while cont < 100:
    soma = soma + (2**(-cont))
    cont = cont + 1
print soma