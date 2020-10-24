deposito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros: "))
mes = 1
deposito = 0
while mês <= 24:
    deposito = deposito + (deposito * (taxa))
    print ("Saldo do" ,mes, deposito)
    mes = mes + 1
print (mes, deposito)