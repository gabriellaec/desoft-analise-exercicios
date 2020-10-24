deposito_inicial = int(input("Depósito inicial: "))
taxa_juros = int(input("Taxa de juros (%): "))
meses = 0
valor = deposito_inicial * ((1+(taxa_juros/100)**meses))
while meses < 24:
    print("{0:.2f}".format(valor))
    valor = deposito_inicial * ((1 + (taxa_juros / 100) ** meses))
    meses += 1
print("{0:.2f}".format(valor))