mes = 0
deposito = 0
deposito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros: "))
while mes <= 24:
    deposito = deposito + (deposito*(taxa/100))
    print ("Saldo do" ,mes, deposito)
    mes = mes + 1
print (mes)
print(deposito)