mes = 0
deposito = 0
deposito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros: "))
saldo = deposito
while mes <= 24:
    saldo = saldo + (saldo*(taxa/100))
    print ("Saldo do" ,mes, saldo)
    mes = mes + 1

print(saldo - deposito)