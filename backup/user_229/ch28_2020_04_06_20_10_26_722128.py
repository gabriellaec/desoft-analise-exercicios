i = 0
total = valor
while i >= 99:
    total += valor
    valor = valor/2**i
    i += 1
print("O resultado é {0}".format(total))

