deposito_inicial = int(input("Depósito inicial: "))
taxa_juros = int(input("Taxa de juros (%): "))
meses = 0
valor = deposito_inicial * ((1+(taxa_juros/100))**meses)
while meses < 25:
    print("{0:.2f}".format(valor))
    meses += 1
    valor = valor * ((1 + (taxa_juros / 100) ** meses))
print("Total: {0:.2f}".format(valor))