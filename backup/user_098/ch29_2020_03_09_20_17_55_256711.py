deposito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros: "))
i = 1
saldo = deposito
while i <= 24:
    saldo = saldo + (saldo*(taxa/100))
    print("{0:.2f}" .format(saldo))
    print(i)
    i = i+1
print("{0:.2f}" .format(saldo-deposito))