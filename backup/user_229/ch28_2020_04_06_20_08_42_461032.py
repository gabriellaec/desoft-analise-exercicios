valor = 1
total = valor
while valor >= (1/(2**99)):
    total += valor
    valor = valor/2
print("O resultado é {0}".format(valor))

