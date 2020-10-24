mes = 0
deposito = 0
deposito = float(input("Depósito inicial: "))
deposito = saldo
taxa = float(input("Taxa de juros: "))
while mes <= 24:
    saldo = saldo + (saldo*(taxa/100))
    print ("Saldo do" ,mes, deposito)
    mes = mes + 1

print(saldo - deposito)