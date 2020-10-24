valor = 1
total = 0
while valor >= (1%2**99):
    total = total + valor
    valor = valor%2
print("O resultado é {0}".format(valor))