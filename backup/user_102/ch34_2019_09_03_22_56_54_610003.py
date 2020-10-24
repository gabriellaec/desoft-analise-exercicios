mes = 0
deposito = 0
deposito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros: "))
saldo = deposito
while mes < 24:
    saldo = saldo + (saldo*(taxa/100))
    print (mes)
    mes = mes + 1

print(saldo - deposito)